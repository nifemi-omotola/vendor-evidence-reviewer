# Vendor Evidence Reviewer

A Claude skill that helps procurement and third-party review teams check **one vendor's** RFI/RFP submission against the organisation's own requirements.

It:

- assesses each answer and the supporting evidence against the requirements in your questionnaire, plus any criteria you supply, and never invents its own
- finds missing evidence, weak evidence and contradictions between documents
- checks the vendor's key claims online (for example certificates), and marks each one as corroborated, contradicted or could not be verified
- produces a report that opens in your browser, with a **Save as Word document** button

> The report is advisory. It is not a procurement decision, an audit opinion or a certification, and it doesn't replace legal, security, financial or specialist review.

## What you need

- A Claude plan that supports Skills (Pro, Max, Team or Enterprise). On Team or Enterprise, an administrator may need to allow Skills first.
- **Code execution and file creation** switched on. The skill uses it to build the report.
- **Web search** switched on, so the skill can verify claims online. Without it, the report says that external verification was not performed.

## Install

### Claude (claude.ai or the desktop app)

1. Download **[vendor-evidence-reviewer.zip](vendor-evidence-reviewer.zip)**. On the file page, click the download button. Don't unzip it.
2. In Claude, go to **Settings → Capabilities**.
3. Make sure **Code execution and file creation** is on.
4. In the **Skills** section, click **Upload skill** and choose the zip.
5. Check that **vendor-evidence-reviewer** appears in your Skills list and its toggle is on.

To update to a newer version later, delete the old skill from the list and upload the new zip.

### Claude Code

Copy the skill folder into your personal skills folder, then start a new session:

```bash
git clone https://github.com/nifemi-omotola/vendor-evidence-reviewer.git
cp -R vendor-evidence-reviewer/vendor-evidence-reviewer ~/.claude/skills/
```

## How to use it

1. Start a **new chat**, with one vendor per chat.
2. Upload the questionnaire/RFI, the vendor's completed response, and the vendor's supporting documents (Word, PDF, Excel, etc.).
3. Ask in your own words, for example: *"Please assess this vendor's response against our RFI requirements."* You don't need to name the skill. If Claude doesn't pick it up, add "use the vendor-evidence-reviewer skill".
4. **Answer the assessment-basis question.** Before assessing anything, the skill asks whether you have organisation-specific benchmarks or criteria. Upload them, or say you have none and confirm that it may use only the questionnaire's requirements.
5. Wait while it reads the documents and checks claims online. This can take several minutes.
6. **Open the report** (an HTML file) in your browser. Click **Save as Word document** to keep a copy, or **Print / Save as PDF**.

**Tip:** to skip step 4, say up front: *"We have no extra benchmarks, use only the questionnaire, go ahead."*

## What the report contains

| Section | What you'll find |
|---|---|
| Header | Vendor, assessment date, materials reviewed, assessment basis, whether online checks were done |
| 1. Executive summary | The overall result and the most important findings |
| 2. Requirement-by-requirement table | For each requirement: the vendor's answer, the evidence, the assessment (Satisfactory / Needs clarification / Unsatisfactory), the online check and the next action |
| 3. Key gaps and contradictions | Only the material issues, and why they matter |
| 4. External verification | Which claims were checked, the sources, and the outcome |
| 5. Follow-up questions | Neutral questions you can send to the vendor |
| 6. Overall recommendation | Proceed / Proceed with caution / Not recommended to proceed, with the reasons |

## Good practice and limitations

- **Confidentiality:** only upload real vendor documents if your organisation's policy allows them to be used with Claude.
- **One vendor at a time:** the skill does not compare or rank vendors.
- **Online checks:** if a claim can't be found online, the skill reports it as "could not be verified", not as false.
- **Check the findings:** every finding is linked to a document and section. Spot-check the important ones before acting on them.

## What's in this repository

| Path | Contents |
|---|---|
| `vendor-evidence-reviewer/SKILL.md` | The skill's instructions |
| `vendor-evidence-reviewer/scripts/build_report.py` | Turns the Markdown report into the browser page with the Word and PDF buttons (Python standard library only) |
| `vendor-evidence-reviewer.zip` | The same skill folder, zipped and ready to upload to Claude |

## Feedback

Found a problem or have a suggestion? Please [open an issue](../../issues).

## Licence

Released under the [MIT License](LICENSE).
