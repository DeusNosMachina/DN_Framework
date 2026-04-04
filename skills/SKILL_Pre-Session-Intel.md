---
name: pre-session-intel
description: "Pre-populate a Growth Blueprint board with public intelligence before a client session. Use when the user says 'prep for [client]', 'pre-session intel', 'research [company]', 'get me ready for [meeting]', or wants public data gathered before a Growth Blueprint session. Pulls public information and maps it to board sections with dimensional tags. The goal: walk into every meeting with a board that already shows you understand them."
---

# Pre-Session Intelligence Agent

## Purpose

Before a client session, deploy this skill to gather public intelligence and pre-populate the client's `board-state.md` with dimensionally tagged artifacts. The client sees a board that already reflects their reality. The facilitator starts from context (3D), not from scratch (1D).

## What Gets Gathered

### Tier 1: Always Available (Web Search)
- Company overview, founding, leadership, mission statement
- Industry classification and competitive landscape
- Recent news, press releases, strategic announcements (last 6-12 months)
- Job postings (reveal organizational priorities, growth areas, capability gaps)
- Public-facing messaging (homepage, about page, product pages)

### Tier 2: Public Companies (SEC / Financial)
- Revenue, margins, growth trajectory (from 10-K, earnings, public filings)
- Strategic priorities from earnings calls and investor presentations
- Competitive positioning from MD&A sections
- Risk factors (what they're worried about — direct shadow intelligence)

### Tier 3: Market Context
- Industry trends affecting this company
- Key competitors and their positioning
- Market size estimates if available

## Where It Maps on the Board

| Data Found | Board Section | Dimension | Pillar |
|-----------|---------------|-----------|--------|
| Mission statement, values | Section 2: Brand Identity | 💗1D / 🟩5D | Heart |
| Revenue, financials, metrics | Section 6: KPI Dashboard | 🔵2D | Truth |
| Competitive landscape | Section 1: Business Model (Zone 1.2) | 🔵2D / 🟣3D | Truth / Nuance |
| Market size, TAM | Section 1: Business Model (Zone 1.3) | 🔵2D | Truth |
| Product/service description | Section 7: Product-Market Fit | 🟣3D | Nuance |
| Customer descriptions (from website) | Section 3: Customer Profile | 🟣3D | Nuance |
| Job postings → team structure | Section 4: Roles & Responsibilities | 🟣3D | Nuance |
| Strategic announcements | Section 5: Goals & Priorities | 🟩5D | Heart / Truth |
| Risk factors (10-K) | Section 5: Biggest Risks (Zone 5.3) | 🔴Shadow | Truth |
| Industry trends | Parking Lot (Zone D) | 🟣3D / ⬛9D | Nuance |

## Execution Protocol

1. **Get the basics.** Company name, website, ticker (if public), industry. The user provides this or you search for it.

2. **Run searches.** Web search for: company overview, recent news, competitive landscape, job postings. If public company: search for recent SEC filings, earnings summaries.

3. **Read the company's own website.** Their homepage, about page, and product pages contain their self-described identity (5D), value propositions (Section 1), and customer targeting (Section 3).

4. **Map findings to board sections.** Each piece of intelligence becomes a dimensionally tagged artifact in the board-state.md. Use the mapping table above.

5. **Tag confidence levels.** Public data from official filings = high confidence (🔵2D, solid). Inferences from job postings or marketing language = medium confidence (🟣3D, contextual). Speculation = low confidence, mark explicitly and park in Zone D.

6. **Flag shadow signals.** Risk factors, negative press, Glassdoor themes, high executive turnover — these are shadow artifacts. Tag with 🔴 and note them separately. Don't bury them.

7. **Write to the client's board-state.md.** Pre-populate the relevant sections. Mark every artifact as `[PRE-SESSION INTEL]` so the facilitator knows what was researched vs. what was co-created with the client.

8. **Create a briefing summary.** At the top of the session file, write a 1-paragraph briefing: who they are, what they're facing, what's interesting, what the facilitator should probe on. This is your 30-second prep read.

## What NOT to Do

- Don't access anything that requires authentication or credentials
- Don't scrape employee personal information
- Don't present inferences as facts — always tag confidence
- Don't over-populate — 3-5 artifacts per section max. Leave room for the client to fill in what you couldn't find. The board should feel *informed*, not *finished*
- Don't skip shadow signals — risk factors and negative signals are the most valuable pre-session intelligence. They're what the client won't volunteer until trust is established.

## Output

The pre-populated `board-state.md` and a briefing paragraph in the first session file. The facilitator reads the briefing, scans the board, and walks into the meeting already at 3D (context) instead of 1D (spark).

## Integration

This skill is invoked from within a Growth Blueprint session. Typical flow:

```
User: "growth blueprint, set up codename anvil for [Company], they're a [industry] company"
→ growth-blueprint skill scaffolds the client workspace
→ pre-session-intel skill gathers public data and populates the board
→ User reviews the pre-populated board before the meeting
→ Session begins with context already established
```
