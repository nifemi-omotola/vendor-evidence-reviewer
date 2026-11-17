#!/usr/bin/env python3
"""Turn a Markdown vendor assessment report into a browser-viewable HTML page.

The page has two buttons:
  - "Save as Word document": downloads the report as a Word file (.doc) that
    opens in Microsoft Word, Pages, Google Docs or LibreOffice.
  - "Print / Save as PDF": opens the browser's print dialog.

Standard library only (Python 3.8+), so it runs anywhere without installs.

Usage:
    python3 build_report.py report.md [--output report.html] [--open]
"""

import argparse
import html
import re
import sys
import webbrowser
from pathlib import Path

# --------------------------------------------------------------------------
# Inline Markdown
# --------------------------------------------------------------------------

BADGES = {
    # assessment labels
    "satisfactory": ("#e6f4ea", "#1e6b34"),
    "needs clarification": ("#fff4e0", "#8a5300"),
    "unsatisfactory": ("#fde8e8", "#a12020"),
    # overall recommendation
    "proceed": ("#e6f4ea", "#1e6b34"),
    "proceed with caution": ("#fff4e0", "#8a5300"),
    "not recommended to proceed": ("#fde8e8", "#a12020"),
}


def _badge(match):
    text = match.group(1)
    colours = BADGES.get(text.strip().rstrip(".:").lower())
    if not colours:
        return match.group(0)
    bg, fg = colours
    return (
        '<strong class="badge" style="background:%s;color:%s;'
        'padding:1px 6px;border-radius:4px;white-space:nowrap">%s</strong>'
        % (bg, fg, text)
    )


def inline(text):
    """Convert inline Markdown (links, bold, italic, code) to HTML."""
    placeholders = []

    def stash(fragment):
        placeholders.append(fragment)
        return "\x00%d\x00" % (len(placeholders) - 1)

    text = html.escape(text, quote=False)
    # allow explicit line breaks inside table cells
    text = re.sub(r"&lt;br\s*/?&gt;", lambda m: stash("<br>"), text)
    # inline code
    text = re.sub(r"`([^`]+)`", lambda m: stash("<code>%s</code>" % m.group(1)), text)
    # [label](url)
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
        lambda m: stash(
            '<a href="%s" target="_blank" rel="noopener">%s</a>'
            % (m.group(2).replace('"', "%22"), m.group(1))
        ),
        text,
    )
    # bare URLs
    text = re.sub(
        r"(?<![\"'=])(https?://[^\s<>()]+[^\s<>().,;:!?'\"])",
        lambda m: stash(
            '<a href="%s" target="_blank" rel="noopener">%s</a>'
            % (m.group(1).replace('"', "%22"), m.group(1))
        ),
        text,
    )
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__(.+?)__", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"<strong>([^<]+)</strong>", _badge, text)

    return re.sub(r"\x00(\d+)\x00", lambda m: placeholders[int(m.group(1))], text)


# --------------------------------------------------------------------------
# Block Markdown
# --------------------------------------------------------------------------

TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
LIST_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    cells, current, in_code = [], "", False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            current += "|"
            i += 2
            continue
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(current.strip())
            current = ""
        else:
            current += ch
        i += 1
    cells.append(current.strip())
    return cells


def render_table(rows):
    header, body = rows[0], rows[1:]
    out = ['<div class="table-wrap"><table>', "<thead><tr>"]
    out += ["<th>%s</th>" % inline(c) for c in header]
    out.append("</tr></thead><tbody>")
    for row in body:
        row = (row + [""] * len(header))[: len(header)]
        out.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in row) + "</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def render_list(items):
    """items: list of (indent, ordered, text). Supports nesting by indentation."""
    out, stack = [], []  # stack of (indent, tag)
    for indent, ordered, text in items:
        tag = "ol" if ordered else "ul"
        while stack and indent < stack[-1][0]:
            out.append("</li></%s>" % stack.pop()[1])
        if not stack or indent > stack[-1][0]:
            out.append("<%s>" % tag)
            stack.append((indent, tag))
        else:
            out.append("</li>")
        out.append("<li>%s" % inline(text))
    while stack:
        out.append("</li></%s>" % stack.pop()[1])
    return "".join(out)


def markdown_to_html(md):
    lines = md.replace("\r\n", "\n").split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            i += 1
            code = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>%s</code></pre>" % html.escape("\n".join(code)))
            continue

        m = HEADING.match(line)
        if m:
            level = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (level, inline(m.group(2)), level))
            i += 1
            continue

        if re.match(r"^\s*([-*_])(\s*\1){2,}\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        if "|" in line and i + 1 < len(lines) and TABLE_SEP.match(lines[i + 1]):
            rows = [split_row(line)]
            i += 2
            while i < len(lines) and lines[i].strip() and "|" in lines[i]:
                rows.append(split_row(lines[i]))
                i += 1
            out.append(render_table(rows))
            continue

        if LIST_ITEM.match(line):
            items = []
            while i < len(lines):
                lm = LIST_ITEM.match(lines[i])
                if lm:
                    ordered = lm.group(2)[0].isdigit()
                    items.append((len(lm.group(1).expandtabs(4)), ordered, lm.group(3)))
                    i += 1
                elif lines[i].strip() and lines[i].startswith((" ", "\t")) and items:
                    # continuation of the previous item
                    ind, ordd, txt = items[-1]
                    items[-1] = (ind, ordd, txt + " " + lines[i].strip())
                    i += 1
                else:
                    break
            out.append(render_list(items))
            continue

        if stripped.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>%s</blockquote>" % "<br>".join(inline(q) for q in quote))
            continue

        # paragraph: keep each source line on its own line (metadata blocks rely on it)
        para = []
        while i < len(lines):
            l = lines[i]
            if (
                not l.strip()
                or HEADING.match(l)
                or LIST_ITEM.match(l)
                or l.strip().startswith((">", "```"))
                or ("|" in l and i + 1 < len(lines) and TABLE_SEP.match(lines[i + 1]))
            ):
                break
            para.append(inline(l.strip()))
            i += 1
        out.append("<p>%s</p>" % "<br>".join(para))

    return "\n".join(out)


# --------------------------------------------------------------------------
# Page template
# --------------------------------------------------------------------------

REPORT_CSS = """
body { font-family: Calibri, "Segoe UI", Arial, sans-serif; font-size: 11pt; color: #1f2328; line-height: 1.45; }
h1 { font-size: 20pt; margin: 0 0 12px; color: #13294b; }
h2 { font-size: 14pt; margin: 24px 0 8px; color: #13294b; border-bottom: 1px solid #d0d7de; padding-bottom: 4px; }
h3 { font-size: 12pt; margin: 18px 0 6px; color: #13294b; }
p { margin: 6px 0; }
ul, ol { margin: 6px 0 6px 22px; padding: 0; }
li { margin: 3px 0; }
table { border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: 8px 0 14px; }
th, td { border: 1px solid #c9d1d9; padding: 6px 7px; vertical-align: top; text-align: left; }
th { background: #eef2f7; font-weight: bold; }
a { color: #0b57d0; word-break: break-word; }
code { font-family: Consolas, monospace; font-size: 9.5pt; background: #f2f4f7; padding: 0 3px; }
pre { background: #f2f4f7; padding: 10px; overflow-x: auto; }
blockquote { margin: 8px 0; padding: 6px 12px; border-left: 3px solid #c9d1d9; color: #444; }
hr { border: 0; border-top: 1px solid #d0d7de; margin: 16px 0; }
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
__REPORT_CSS__
html { background: #eef0f3; }
body { margin: 0; }
.toolbar { position: sticky; top: 0; z-index: 10; background: #13294b; color: #fff;
  display: flex; flex-wrap: wrap; align-items: center; gap: 10px; padding: 10px 16px;
  font-family: "Segoe UI", Arial, sans-serif; font-size: 13px; }
.toolbar .name { flex: 1 1 auto; min-width: 0; opacity: .85; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.toolbar button { font: inherit; cursor: pointer; border: 0; border-radius: 6px; padding: 8px 14px; }
.toolbar .primary { background: #fff; color: #13294b; font-weight: 600; }
.toolbar .secondary { background: transparent; color: #fff; border: 1px solid rgba(255,255,255,.6); }
.page { background: #fff; max-width: 1100px; margin: 20px auto; padding: 36px 44px;
  box-shadow: 0 1px 4px rgba(0,0,0,.12); box-sizing: border-box; }
.table-wrap { overflow-x: auto; }
@media (max-width: 700px) { .page { margin: 0; padding: 20px 16px; box-shadow: none; } }
@media print {
  html { background: #fff; }
  .toolbar { display: none; }
  .page { margin: 0; padding: 0; box-shadow: none; max-width: none; }
  @page { size: A4 landscape; margin: 15mm; }
  tr { page-break-inside: avoid; }
}
</style>
</head>
<body>
<div class="toolbar">
  <span class="name">__TITLE__</span>
  <button class="primary" id="save-word" type="button">Save as Word document</button>
  <button class="secondary" type="button" onclick="window.print()">Print / Save as PDF</button>
</div>
<div class="page" id="report">
__BODY__
</div>
<script>
(function () {
  var FILE_NAME = __FILE_NAME__;
  var REPORT_CSS = __REPORT_CSS_JSON__;
  document.getElementById('save-word').addEventListener('click', function () {
    var body = document.getElementById('report').innerHTML;
    var doc =
      '<html xmlns:o="urn:schemas-microsoft-com:office:office" ' +
      'xmlns:w="urn:schemas-microsoft-com:office:word" ' +
      'xmlns="http://www.w3.org/TR/REC-html40">' +
      '<head><meta charset="utf-8"><title>' + document.title + '</title>' +
      '<!--[if gte mso 9]><xml><w:WordDocument><w:View>Print</w:View>' +
      '<w:Zoom>100</w:Zoom></w:WordDocument></xml><![endif]-->' +
      '<style>' + REPORT_CSS +
      '@page Section1 { size: 841.9pt 595.3pt; mso-page-orientation: landscape; margin: 54pt 54pt 54pt 54pt; }' +
      'div.Section1 { page: Section1; }' +
      '</style></head><body><div class="Section1">' + body + '</div></body></html>';
    var blob = new Blob(['\\ufeff', doc], { type: 'application/msword' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = FILE_NAME;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 1000);
  });
})();
</script>
</body>
</html>
"""


def build(md_text, title, doc_name):
    import json

    body = markdown_to_html(md_text)
    page = PAGE.replace("__REPORT_CSS_JSON__", json.dumps(REPORT_CSS))
    page = page.replace("__REPORT_CSS__", REPORT_CSS)
    page = page.replace("__FILE_NAME__", json.dumps(doc_name))
    page = page.replace("__TITLE__", html.escape(title))
    return page.replace("__BODY__", body)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("markdown", help="Path to the Markdown report")
    parser.add_argument("--output", "-o", help="Where to write the HTML (default: next to the Markdown file)")
    parser.add_argument("--open", action="store_true", help="Open the report in the default browser")
    args = parser.parse_args()

    src = Path(args.markdown)
    md_text = src.read_text(encoding="utf-8")
    out = Path(args.output) if args.output else src.with_suffix(".html")

    m = re.search(r"^#\s+(.+)$", md_text, re.M)
    title = re.sub(r"[*_`]", "", m.group(1)).strip() if m else src.stem
    doc_name = out.stem + ".doc"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(md_text, title, doc_name), encoding="utf-8")
    print("Report written to: %s" % out.resolve())

    if args.open:
        opened = False
        try:
            opened = webbrowser.open(out.resolve().as_uri())
        except Exception:
            opened = False
        print("Opened in browser." if opened else "Could not open a browser here; open the file above manually.")


if __name__ == "__main__":
    sys.exit(main())
