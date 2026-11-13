# Job search run: 13 Nov 2026

Source profile: danielori.website, the /resume page and the master CV PDF (Daniel-Ori-Resume.pdf).
Fit summary: 9 years of product design (2017 to now), senior level, B2B/fintech/internal tools/AI. Based in Liverpool; MA at LJMU 2026–27.

## What was searched and why there are no part-time roles

The README brief asks for **part-time (20 h/week) remote** UK roles. I searched:
- Reed, Indeed UK, Glassdoor, Adzuna, CharityJob, Twine and Remote Rocketship (via web search; Indeed and Adzuna block automated access)
- LinkedIn public job search for UK product/UX design roles posted in the last 30 days
- Public Greenhouse, Ashby and Lever boards for about 100 UK fintech, healthtech and SaaS companies
- Liverpool and Manchester-specific searches

I found **no live, UK-based, part-time product design role where you would be employed by the company** at the right level. The part-time hits were US-only, freelance or contractor work (a Student visa does not allow self-employment), expired (for example ReCulture Liverpool, closed), or brand/graphic roles. So the three picks below are **full-time hybrid roles in Manchester**, about 50 minutes from Liverpool by train. Each is an unusually close match to your portfolio. Before you apply, read the right-to-work note.

> **Right-to-work check (only you can answer this).** If you are on a Student visa, term-time work is capped at 20 h/week, and you cannot fill a permanent full-time vacancy until your course ends (or until you switch to Graduate or Skilled Worker status). Each form below asks you to declare your right to work and whether you need sponsorship, and those are legal statements. I have **not** submitted anything for that reason. You could ask each employer about a 0.5 FTE arrangement or a start date after your MA. Medius's salary (£44–47k) is above the general Skilled Worker threshold, so that conversation is realistic.

---

## 1. Medius: Product Designer (Manchester or London, hybrid). Fit: excellent
- Link: https://career.medius.com/jobs/8355161-product-designer
- £44,000–£47,000. Accounts payable, invoicing and payments automation with AI. 2+ years required, ideally B2B SaaS or fintech.
- Why you stand out: their "nice to haves" are **approval flows, complex data workflows and financial products**, which describes your AFaaS case study almost exactly. They also want designers who design AI features (Rana Studio).
- CV: `Daniel-Ori-CV-Medius-Product-Designer.pdf`
- **Status: pending your action.** The form is straightforward (Teamtailor, no CAPTCHA seen) but needs details only you can give:
  - Home address (required)
  - Salary expectation (required). Suggestion: "£47,000 base, flexible for the right scope."
  - Sponsorship question: Yes or No (see the note above)
  - Location: tick **Manchester**
- Draft answers:
  - *Portfolio:* https://danielori.website (lead with /work/afaas-payment-portal)
  - *What kind of products or problems do you enjoy working on?* "Products where the rules are complicated, the users are not alike, and a wrong decision costs somebody something real. Most recently that has been AFaaS at Babban Gona: an 8-module payment portal where finance teams start, review and approve payments. The interesting work was not the form but the control model: separating makers from controllers, giving single and batch payments the same review checkpoint, and turning generic error badges into actionable states. I'd love to bring that to AP and payments at Medius, especially where AI is taking over the manual work and people still need to trust what it did."
  - *How do you know when your design is successful?* "I agree what success means before I design: a task-completion or error measure, plus the risk we are trying to remove. For AFaaS that meant invalid entries caught before submission and fewer manual follow-ups after an audit query. I prepare A/B variants and test plans so we can measure, and I treat targets as targets until the analytics confirm them. Shipped and used without support is the bar, not approved in Figma."

## 2. Anaplan: Product Designer (Manchester office). Fit: strong
- Link: https://job-boards.greenhouse.io/anaplan/jobs/8643429002
- Enterprise planning SaaS. The role owns a feature area spanning data-rich workflows and agentic and generative AI, within a team of 25+ designers and researchers and a mature design system.
- Why you stand out: you have proven experience with "data-rich, workflow-heavy interfaces" (AFaaS, Figorr's 500+ screen, three-portal system) and with AI-assisted experiences (Rana Studio). The nice-to-haves (HTML/CSS, financial systems, complex B2B) all match.
- CV: `Daniel-Ori-CV-Anaplan-Product-Designer.pdf`
- **Status: pending your action.** The form is on Greenhouse and needs:
  - Your legal name and full postal address
  - Two right-to-work and sponsorship declarations
  - Some Greenhouse boards add a reCAPTCHA on submit
- How did you hear: "LinkedIn"

## 3. Mark43: Senior Product Designer, UK RMS (Manchester, hybrid 3 days a week). Fit: strong on experience, likely blocked on visa
- Link: https://job-boards.greenhouse.io/mark43/jobs/8383879 (also on mark43.com/list-job/8383879)
- Police records-management software for UK forces. Requires 7+ years in complex, accuracy-critical enterprise workflows. Up to 25% travel.
- Why you stand out: 9 years of experience, 0-to-1 work (Figorr, CTCare), and role, permission and audit-heavy operational design (AFaaS).
- CV: `Daniel-Ori-CV-Mark43-Senior-Product-Designer.pdf`
- **Status: likely blocker.** The listing says: "Applicants must be authorized to work for any employer… We are unable to sponsor or take over sponsorship." A Student visa does not meet that. Only apply if you hold unrestricted right to work (for example ILR, a dependant visa, or Global Talent). UK policing work may also need police vetting, which can require a few years of UK residence.
- Draft answers if you are eligible:
  - 7+ years: Yes (2017 to present)
  - Enterprise software: "Internal tools and an 8-module finance-operations platform at Babban Gona; CTCare, enterprise leave management for Cavista and Axxess; Figorr admin and owner portals."
  - SaaS company: Yes (Figorr, Cavista/Axxess)
  - Led design research: Yes. Figorr discovery covered 15 owners, 20 customers and 5 site inspections.
  - 0-to-1: "Figorr CCI, a six-month programme from customer-zero concepts to three connected portals; CTCare, from hackathon concept to production development."
  - Portfolio: https://danielori.website, password N/A

---

## What was changed in each CV (truthful reordering only, no new claims)
- **Medius:** the headline, profile and first bullets lead with payments, approval flows, maker/controller controls, batch and exception states, and AI. The strengths section mirrors their requirements: Figma components, variants and auto layout; design-system contribution; research.
- **Anaplan:** the headline focuses on data-rich enterprise workflows and AI. Rana Studio is moved to the first bullet. The CV highlights HTML/CSS and Computer Science, plus WCAG, discovery and workshops.
- **Mark43:** written for a senior role, with an emphasis on accuracy-critical operational software, role, permission and audit design, 0-to-1 work and leading research.
- All three now say "Liverpool, UK · commutable to Manchester". Rebuild with `python3 build_cvs.py`, then print the HTML to PDF.
