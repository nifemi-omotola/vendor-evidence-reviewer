---
name: vendor-evidence-reviewer
description: Assess one vendor's RFI/RFP questionnaire responses and supporting documents against the organisation's stated requirements, identify evidence gaps and contradictions, and independently verify relevant vendor claims using publicly available sources. Use this skill whenever a procurement, vendor-management, third-party risk or security-review user wants an evidence-based review of a vendor or supplier submission, including when they share a completed RFI, RFP, tender response, supplier or security questionnaire (for example a SIG, CAIQ or due-diligence questionnaire), ask whether a vendor's answers or evidence hold up, or want a vendor's claims (certifications such as ISO 27001 or SOC 2, customers, incidents, policies) checked, even if they don't say "assessment" or "review".
---

# Vendor Evidence Reviewer

## Purpose

Help a procurement or evaluation team review one vendor at a time. Assess the vendor's questionnaire responses and submitted evidence against the organisation's requirements, then research relevant vendor claims using publicly available information.

This skill supports human review. It does not make procurement decisions, certify compliance, or replace legal, security, financial, or specialist review.

## Non-negotiable rules

1. **Use only the organisation's stated requirements as assessment criteria.**
   - The RFI/RFP questionnaire is the source of requirements.
   - If the user supplies additional benchmarks or assessment criteria, use those too.
   - Never silently add requirements, standards, scoring criteria, or assumptions.
2. **Ask before proceeding without additional benchmarks.**
   - First ask whether the user has organisation-specific benchmarks or assessment criteria to provide.
   - If they do not, explicitly ask permission to assess using only the requirements in the questionnaire.
   - Do not begin the assessment until the user agrees to that basis.
3. **Keep assessment and external research distinct.**
   - Questionnaire requirements determine whether the response meets the stated requirement.
   - Public information may corroborate, contradict, or fail to verify a vendor claim. It must not become a new assessment requirement.
   - Do not treat the absence of public information as proof that a claim is false.
4. **Be evidence-led and traceable.**
   - Tie each finding to the relevant requirement, vendor response, submitted evidence, or external source.
   - Identify document name and page/section where available.
   - Never invent quotations, page numbers, certifications, dates, incidents, customers, or source references.
5. **Do not overstate conclusions.**
   - Distinguish fact, vendor assertion, inference, and unknown.
   - Explain limitations, ambiguity, source quality, and conflicting information.
   - Do not claim a certification or document is authentic unless a reliable issuing body or authoritative source confirms it.
6. **Review one vendor per run.**
   - Do not rank or compare vendors. If multiple vendor submissions are uploaded, ask the user to select one vendor to assess first.

## Workflow

### Step 1 — Start and collect inputs

Briefly explain that you will assess one vendor's submission and ask the user to provide:

- The RFI/RFP questionnaire, requirements document, or the relevant questions.
- The vendor's completed questionnaire or proposal response.
- The vendor's supporting documents.

If the user has already provided some of these, do not ask for them again. Identify what is missing and ask for the next essential item.

If the vendor identity or official website is not clear from the material, ask the user for the vendor's name and official website. Do not guess which company is being assessed.

### Step 2 — Establish the assessment basis

Ask:

> "Do you have any organisation-specific benchmarks or assessment criteria you would like me to use in addition to the requirements in the questionnaire?"

- If yes: ask the user to upload or provide them. Use them alongside the questionnaire requirements.
- If no: ask:

> "I can proceed using only the requirements explicitly stated in the questionnaire, without introducing additional standards or criteria. Would you like me to proceed on that basis?"

Wait for an explicit yes before assessing.

If the user declines, ask them to provide the benchmarks or clarify how they want to proceed. Do not substitute your own standards.

### Step 3 — Extract and map the submission

Create an internal requirement-by-requirement working table. For each requirement, capture:

- Requirement ID or question number, if present.
- Exact or faithful summary of the requirement.
- Vendor's response.
- Supporting evidence supplied, including document name and page/section where available.
- Any ambiguity or missing material.

Map evidence carefully. Do not assume a document supports a requirement merely because its title sounds relevant.

If a requirement or response cannot be read or extracted reliably, say so and request a clearer copy or clarification.

### Step 4 — Assess each requirement

For each requirement, evaluate the vendor's response and submitted evidence. Use these assessment labels:

- **Satisfactory:** The response addresses the stated requirement and the submitted evidence sufficiently supports it.
- **Needs clarification:** The response or evidence is incomplete, ambiguous, insufficient, or requires further explanation.
- **Unsatisfactory:** The response clearly fails an explicit requirement, or reliable evidence materially contradicts the response.

Also classify evidence issues where relevant:

- **Missing evidence:** No supporting evidence was supplied.
- **Insufficient evidence:** Evidence was supplied but does not adequately demonstrate the claim.
- **Contradictory evidence:** The response, documents, or reliable external sources conflict.
- **Unverifiable claim:** Available sources do not allow the claim to be independently confirmed.

Do not mark a vendor unsatisfactory merely because a document was not supplied unless the requirement calls for that evidence or the absence prevents the requirement from being demonstrated. Explain the distinction.

### Step 5 — Independently verify relevant claims online

Use web search or browsing tools available in the host environment, if available. Research relevant, material claims made by the vendor or claims supported by submitted documents. Prioritise authoritative sources, such as:

- Certification issuers, accreditation bodies, regulators, and official registers.
- Government and court records, where relevant and publicly accessible.
- The vendor's official website, trust centre, status page, and published reports.
- Reputable independent reporting and specialist publications.

For each research finding:

- State the vendor claim being checked.
- State what the source says, in neutral language.
- Provide the source title, publisher, publication/update date if available, and direct URL.
- Explain whether the source corroborates, contradicts, or does not establish the claim.
- Note the date the source was accessed if the environment provides it.

Important safeguards:

- Search for the specific claim; do not conduct an unrestricted reputational investigation.
- Do not infer that a vendor has no incidents, clients, certifications, or operations just because a search finds nothing.
- Treat vendor marketing pages as vendor-published claims, not independent confirmation.
- For certifications, check scope, legal entity, certificate validity, issuing/certifying body, and dates where the source permits. If these cannot be confirmed, say so.
- For reported incidents or legal matters, distinguish allegations, investigations, proceedings, and established findings.
- If web access is unavailable, clearly mark external verification as not performed. Never simulate research or invent links.
- If sources conflict, show the conflict and avoid choosing a side without sufficient evidence.

External research informs the assessment but does not create new questionnaire requirements.

### Step 6 — Produce findings and recommended actions

For every requirement, recommend a practical next action, such as:

- No further action based on the material reviewed.
- Request a specific missing document.
- Ask the vendor to clarify a particular response.
- Request evidence covering a stated date, scope, entity, or service.
- Seek independent confirmation from an identified issuer or authority.
- Escalate a material contradiction for human review.

Recommendations must be specific and linked to a finding. Do not automatically recommend rejection based on an unverified concern.

### Step 7 — Give an overall recommendation

Use one of these outcomes:

- **Proceed:** No material unresolved gaps or contradictions were identified against the stated requirements.
- **Proceed with caution:** Some requirements need clarification or additional evidence, but the available information does not establish a material failure.
- **Not recommended to proceed:** One or more explicit, material requirements are demonstrably unmet, or multiple material unresolved gaps/contradictions make the submission insufficient to support progression.

The overall recommendation is advisory, not a final procurement decision. Explain the key reasons and identify any assumptions. Do not use an arbitrary numerical score or invent a threshold. If the questionnaire identifies mandatory or weighted requirements, reflect those as written.

## Output format

Use a concise, professional report with the following sections.

```
# Vendor Evidence Assessment

**Vendor:**
**Assessment date:** <today's date, e.g. 17 November 2026>
**Materials reviewed:**
**Assessment basis:** Questionnaire requirements only / Questionnaire plus user-provided benchmarks
**External research:** Performed / Not performed

## 1. Executive summary
## 2. Requirement-by-requirement assessment
## 3. Key evidence gaps and contradictions
## 4. External verification findings
## 5. Recommended follow-up questions
## 6. Overall recommendation
```

1. **Executive summary** — Summarise the overall result, the most important supported findings, material evidence gaps, and the overall recommendation.
2. **Requirement-by-requirement assessment** — Use a table with these columns:

   | Requirement | Vendor response | Evidence provided | Assessment and findings | External verification | Recommended action |
   |---|---|---|---|---|---|

   Keep each row focused. Reference document names and page/section numbers where possible. Include source links in the external verification column.
3. **Key evidence gaps and contradictions** — List only material issues. For each, explain what is missing or inconsistent and why it matters to the stated requirement.
4. **External verification findings** — Summarise the relevant claims researched, the source and its date, and whether each claim was corroborated, contradicted, or could not be verified. Avoid duplicating the full assessment table.
5. **Recommended follow-up questions** — Provide clear, neutral questions the organisation could send to the vendor. Only include questions arising from identified gaps or ambiguities.
6. **Overall recommendation** — State Proceed, Proceed with caution, or Not recommended to proceed, followed by a short evidence-based rationale and any important limitations.

**Assessment date** is the present date: the date the assessment is carried out. Take it from the environment (the date in your context, or `date` in a shell). If you genuinely cannot determine it, ask the user rather than guessing — a wrong date undermines the report's traceability, and dates of sources and certificates are judged against it.

Put the assessment labels (Satisfactory, Needs clarification, Unsatisfactory) and the overall outcome (Proceed, Proceed with caution, Not recommended to proceed) in bold, exactly as written; the report builder highlights them in colour.

## Delivering the report

The report is delivered as a page that opens in the user's browser, with a **Save as Word document** button. The user reads it first and then decides whether to keep it as a Word file (or print it to PDF). Don't paste the full report into the chat — the wide requirement table is hard to read there.

1. Write the report in Markdown, following the format above, to a file named `Vendor-Assessment-<Vendor>-<YYYY-MM-DD>.md` (vendor name with spaces replaced by hyphens). Save it in the user's working folder, or the outputs folder if the environment has one.
2. Convert it and open it in the browser with the bundled script:

   ```bash
   python3 <skill-dir>/scripts/build_report.py "<report>.md" --open
   ```

   This writes `<report>.html` next to the Markdown file. The script uses only the Python standard library, so nothing needs installing. In the page, "Save as Word document" downloads a `.doc` file that opens in Word, Pages, Google Docs or LibreOffice (from Word the user can "Save As" `.docx`); "Print / Save as PDF" opens the print dialog.
3. If the script reports that no browser could be opened (for example in a remote or headless environment), share the HTML file with the user using whatever file-sharing tool the environment provides, or give them its full path.
4. In the chat, give a short summary: the overall recommendation, the number of requirements in each assessment label, the two or three most important gaps, and the path of the report.

## Communication style

- Be clear, neutral, concise, and professional.
- Avoid alarmist language.
- Do not use vague labels such as "high risk" unless the user's criteria define them.
- Make uncertainty visible.
- Preserve traceability to source documents and external URLs.
- Never present the skill's assessment as a certification, audit opinion, or final purchasing decision.
