---
title: Ketman Activity Statement - February 2025
date: 2025-03-01
categories:
  - Activity Summary
image: february-activity-2025.jpeg
authors: [blackbigswan]
# featured: true
excerpt: Successes and failures in February 2025
---

We can't publish the full data collection. The reasons are two-fold. Sometimes, it's the privacy that the affected company requires or asks us to grant. Other times, entities involved are still part of ongoing investigative work. Even further, it could lead actors to significantly adapt and make it extremely hard to be spotted. Although, the data publication rules may change in the future.

At the same time, we do try to share any relevant data (like payroll data) with the security community through private channels.

This is the first official monthly summary, so the format will most likely change too. This time, we'll be more qualitative than quantitative to give a better overview of how threat intelligence, incident response, IOCs, and TTPs have worked thus far in the real-life cases we encountered.

## Companies affected

We count a project as affected if:

1. A DPRK IT Worker successfully merged code.
2. A DPRK IT Worker got paid for the contribution.

If we were to relax the metric to only the successful merge, there would be more projects affected.

In February, there were **seven companies/projects directly affected** by DPRK IT Workers.

## Confirmed Threats

We track many "flagged" DPRK IT Workers. The scale of the issue is tremendous. We often joke that GitHub has ten times fewer legitimate developers than DPRK IT Workers. It's not worth counting every single flagged account. We count only accounts that we:

1. Confirmed with the participation of the affected company
2. Reported to the affected company with high certainty (but the company still deals with the issue or decided not to deal with the issue; we'll discuss such instances later)

In February we **confirmed ten DPRK IT Workers.**

## Money transferred to North Korea

In some cases, especially if on-chain data was accessible or the company shared it with us later, we have a pretty good idea of how much money actors managed to siphon out of the company.

In February, **affected projects transferred 50,000 USD total** (that we know of) to DPRK IT Workers.

## Average time of activity in the company

In February, the activity time (time spent working on the project) was surprisingly long. All of the actors found worked within the organization for **at least three months, with the longest engagement spanning four months.** No malicious code implant was detected, but accesses needed to be revoked and post-exploitation services used in at least one case.

## New accounts in the database

We archive all of the data used during and after investigations. It encompasses more than just a threat actor's data dump, but also its underlying connections - and there can be quite a few.

In February, **we collected an additional 100 new, high-confidence and active accounts** in Ketman's internal database. These will power up future investigations significantly.

## Company reaction time

This will be sort of a rant.

The Web3 space doesn't treat the issue seriously at all, while also being the biggest target of it.

Out of the seven affected companies, only a single one reacted with an immediate internal escalation and setting up a "war room." Unfortunately, we can't share which company it was, only that it's one of the Top 300 (by TVL) companies in Web3. Their incident response strategy was perfect and gave us a lot of hope for future outreaches (as this was our first reported finding), but the reality was different.

The remaining companies/projects displayed varying degrees of interest. In some cases, we had trouble establishing communication for days, regardless of multiple approaches. In other cases, the issue was graded as "Informational" at best and relegated to be dealt with "maybe next week." It's worth noting that in a few of these instances, the issue is still not resolved, despite the "next week" deadline and multiple requests for updates.

We will most likely start including a clause in the reports sent that in case of no communication whatsoever, we will be publishing and shaming the project. There's no legal obligation on our side to keep anything private, pre- and post-incident alike. It's a courtesy in reality, but we do want to work with the community, we do want higher security standards and better due diligence on OSS contributors, for the benefit of all open source developers. However - when a project decides to hand-wave the issue, we will start to elevate what we perceive as negligence to maliciousness, and start shaming.

It takes days to find a lead, collect the data, verify it, and compile it into a comprehensive final signals report, then delivered for free. "Maybe next week" is not a proper response to a felony-level problem for an organization.