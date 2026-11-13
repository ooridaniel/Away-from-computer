"""Builds role-tailored one-page CVs (HTML + PDF) from a shared fact base.
All claims come from the master CV (danielori.website/resume) and portfolio case studies."""
import html, json, pathlib, subprocess, sys
OUT = pathlib.Path(__file__).parent

CONTACT = ["oridaniel97@gmail.com", "+44 7466 844813", "Liverpool, UK · commutable to Manchester",
           "danielori.website", "linkedin.com/in/daniel-ori-793020b0"]

ROLES = {
"medius": dict(
  file="Daniel-Ori-CV-Medius-Product-Designer",
  headline="Product designer for payment, approval and AI-assisted workflows in B2B finance.",
  profile=[
    "8+ years designing B2B and fintech products; currently designing payment approval workflows and AI-assisted tools at Babban Gona.",
    "Specialist in approval flows and financial controls: maker/controller separation, batch payments, exception states and audit trails.",
    "Works end-to-end inside a squad, from problem framing and research to Figma prototypes, design-system components and engineering handoff.",
  ],
  exp={
   "babban": ["Designed AFaaS, an 8-module payment portal where finance teams start, review and approve payments to individuals, member groups, transporters and staff.",
              "Replaced a single universal form with distinct payment paths and separated Finance Members (makers) from Financial Controllers (approvers), so the wrong person cannot move money forward.",
              "Designed one control model for single and batch payments, with actionable clean / flagged / invalid / blocked states and an audit record that answers 'what happened' later.",
              "Designed Rana Studio, an AI product for reviewing and recovering AI-generated training content; prepared A/B test variants and a shared component model for engineering."],
   "cavista": ["Led product design for CTCare, a leave-management product spanning employees, managers, the People Team and Finance; won Cavista's 2024 internal hackathon and moved into production development.",
               "Translate business requirements into flows, prototypes and interface specifications for distributed engineering teams."],
   "ulesson": ["Helped deliver Miva University's first official website ahead of launch."],
   "flexisaf": ["Designed education products across web and mobile; tested and refined ideas with wireframes and prototypes."],
   "rosabon": ["Designed financial product experiences and implementation documentation; contributed to early product strategy."],
  },
  project=("Figorr CCI Platform (2023–24)", "Six-month B2B marketplace programme: three connected portals sharing facilities, orders, payments and documents; research with 15 owners and 20 customers; 500+ screens on a tokenised design system."),
  skills=["Approval flows & financial controls","Complex data workflows","AI-powered features & AI-assisted prototyping","User research & usability testing","Figma: components, variants, auto layout","Design-system contribution"],
  tools="Figma, FigJam, Miro, Framer, Webflow, Adobe CC, HTML/CSS, JavaScript",
),
"anaplan": dict(
  file="Daniel-Ori-CV-Anaplan-Product-Designer",
  headline="Product designer for data-rich enterprise workflows and AI-assisted experiences.",
  profile=[
    "8+ years designing complex B2B products; I turn layered rules, roles and edge cases into clear, accessible workflows.",
    "Currently designing internal tools, payment workflows and an AI content product at Babban Gona; Computer Science graduate with HTML/CSS and JavaScript.",
    "Comfortable owning a feature area end-to-end with PMs, engineers and researchers across time zones, inside a shared design system.",
  ],
  exp={
   "babban": ["Designed Rana Studio, an AI product where teams create, review and recover AI-generated training content before it becomes a final video, keeping humans in control of generative output.",
              "Designed AFaaS, an 8-module finance platform: distinct payment paths, maker/controller roles, batch review and actionable exception states for data-heavy operations.",
              "Prepared A/B variants and test plans (sync action, member search and selection) and handed engineering a connected model of steps, roles, statuses and components."],
   "cavista": ["Led product design for CTCare, an enterprise leave-management product across employees, managers, the People Team and Finance; won Cavista's 2024 internal hackathon and moved into production development.",
               "Translate requirements into flows, prototypes and specifications for distributed engineering teams working with a US healthcare-technology partner (Axxess)."],
   "ulesson": ["Helped deliver Miva University's first official website ahead of launch."],
   "flexisaf": ["Designed education products across web and mobile; validated ideas with wireframes and prototypes."],
   "rosabon": ["Designed financial product experiences and implementation documentation; contributed to early product strategy."],
  },
  project=("Figorr CCI Platform (2023–24)", "Admin, owner and customer portals over shared facilities, orders, payments and live telemetry; discovery with 15 owners, 20 customers and five site inspections; 500+ screens, tokens, dark/light themes and responsive states."),
  skills=["Data-rich, workflow-heavy interfaces","AI-assisted & generative experiences","Discovery, interviews, workshops, usability testing","Interaction design & prototyping in Figma","Design-system stewardship","Accessibility (WCAG)","Agile cross-functional delivery"],
  tools="Figma, FigJam, Miro, Framer, Webflow, Adobe CC, HTML/CSS, JavaScript",
),
"mark43": dict(
  file="Daniel-Ori-CV-Mark43-Senior-Product-Designer",
  headline="Senior product designer for high-stakes operational software where accuracy matters.",
  profile=[
    "8+ years designing enterprise and operational software where one wrong decision costs somebody something real.",
    "I make responsibilities, trade-offs and failure paths visible before debating the interface: role-based workflows, exception states and audit records.",
    "Strong on discovery with frontline users, 0-to-1 products and close partnership with PMs and engineers in the UK, US and Africa.",
  ],
  exp={
   "babban": ["Designed AFaaS, an 8-module operational finance system where the wrong person must not move a transaction: role separation, review checkpoints, exception states and an audit trail.",
              "Designed internal tools and Rana Studio (AI content creation, review and recovery) around real operational roles and decisions.",
              "Built reusable interface patterns and handed engineering a connected model of steps, roles, statuses and components."],
   "cavista": ["Led 0-to-1 design for CTCare, a records-heavy leave-management product used by employees, managers, the People Team and Finance; won Cavista's 2024 internal hackathon and moved into production development.",
               "Translate operational requirements into flows, prototypes and specifications for a US healthcare-technology partner (Axxess)."],
   "ulesson": ["Helped deliver Miva University's first official website ahead of launch."],
   "flexisaf": ["Designed education products across web and mobile with developers and stakeholders."],
   "rosabon": ["Designed financial product experiences and implementation documentation; contributed to product strategy."],
  },
  project=("Figorr CCI Platform (2023–24), 0-to-1", "Six-month programme: field research with 15 owners and 20 customers plus five site inspections; three connected portals for verification, orders, payments, documents and live monitoring; 500+ screens."),
  skills=["Complex operational & records workflows","Enterprise SaaS","0-to-1 product design","Leading design research","Role-based permissions & audit","Prototyping & high-fidelity UI","Established design systems (Figma)"],
  tools="Figma, FigJam, Miro, Framer, Webflow, Adobe CC, HTML/CSS, JavaScript",
),
}

JOBS = [("babban","Babban Gona","Senior Product Designer","Remote · Jan 2025 – Present"),
        ("cavista","Cavista (Axxess global partner)","Senior UI/UX Designer","Remote · Apr 2023 – Present"),
        ("ulesson","uLesson Group, for Miva University","Web Designer","Jun 2023 – Mar 2024"),
        ("flexisaf","FlexiSAF Edusoft","Product Designer","Aug 2019 – Dec 2022"),
        ("rosabon","Rosabon Financial Services","UI/UX Designer","Jul 2017 – Aug 2019")]

CSS = """@page{size:A4;margin:10mm 12mm}*{box-sizing:border-box}body{font:9.1pt/1.34 'Helvetica Neue',Arial,sans-serif;color:#1a1a1a;margin:0}
h1{font-size:20pt;margin:0;letter-spacing:-.3px}.hl{font-size:10.5pt;color:#333;margin:2px 0 6px}.ct{font-size:8.6pt;color:#444}
h2{font-size:8.6pt;text-transform:uppercase;letter-spacing:1.2px;border-bottom:1px solid #ddd;padding-bottom:2px;margin:8px 0 4px;color:#155e63}
ul{margin:2px 0 0 0;padding-left:14px}li{margin:1px 0}.job{margin-bottom:6px}.jh{display:flex;justify-content:space-between;font-weight:600}
.jh span{font-weight:400;color:#555;font-size:8.6pt}.role{font-style:italic;color:#333}.sk{columns:2;padding-left:14px}.small{font-size:8.8pt}"""

def page(r):
    e = html.escape
    jobs = "".join(f'<div class="job"><div class="jh">{e(n)}<span>{e(d)}</span></div><div class="role">{e(t)}</div><ul>'
                   + "".join(f"<li>{e(b)}</li>" for b in r["exp"][k]) + "</ul></div>" for k,n,t,d in JOBS)
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Daniel Ori – CV</title><style>{CSS}</style></head><body>
<h1>Daniel Ori</h1><div class="hl">{e(r['headline'])}</div><div class="ct">{' · '.join(map(e,CONTACT))}</div>
<h2>Profile</h2><ul>{''.join(f'<li>{e(p)}</li>' for p in r['profile'])}</ul>
<h2>Experience</h2>{jobs}
<h2>Selected project</h2><div class="small"><b>{e(r['project'][0])}</b>: {e(r['project'][1])}</div>
<h2>Strengths</h2><ul class="sk">{''.join(f'<li>{e(s)}</li>' for s in r['skills'])}</ul>
<h2>Tools</h2><div class="small">{e(r['tools'])}</div>
<h2>Education</h2><div class="small"><b>MA Immersive Media</b>, Liverpool John Moores University (2026–2027, in progress) · <b>BSc Computer Science</b>, Covenant University (2016)<br>
Certificates: Product Design by Google (Udacity, 2023) · Foundations of UX Design (Coursera, 2022) · Webflow 101 (2024)</div>
</body></html>"""

if __name__ == "__main__":
    for key, r in ROLES.items():
        h = OUT / f"{r['file']}.html"; h.write_text(page(r))
    print(json.dumps([str(OUT / (r['file'])) for r in ROLES.values()]))
