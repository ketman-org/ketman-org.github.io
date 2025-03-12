---
title: DPRK IT Workers threat in Open Source Organizations
date: 2025-03-01
categories:
  - DPRK
  - Guides
image: yet-another.jpeg
authors: [blackbigswan]
featured: true
excerpt: Why should you care about the North Korean contributors. Describing risks associated with DPRK IT Workers for organizations.
---

Ketman has been live for a month. The first report is [here](https://ketman.org/february-2025-summary). However, this article isn't about that. It's about North Korean IT worker-related risks to the remote-first open source organizations. The infiltration. The consequences of it, actually. And why you should care where the Pull Request originates from.

### Am I a DPRK IT Worker Target?

**Who they target more:** Remote-first. Open-source. DAOs. Grant-funding. Easy KYC. Crypto payrolls. Early stage. Protocol. Freelance organizations. Community-priority, tech-necessity.

**Who they target less:** Hybrid/On-site. Legal and Cybersec teams on-board. Open-source, but with dedicated code reviewer. Hard KYC/AML/Payroll mandatory. Tech-first, community-second. Late stage. Infrastructure. EDR & Threat Intelligence savvy. 

* Are you hiring remotely from the public hiring pool? (Remote-first)
* Are you accepting pull requests from unknown people? (Open source)
* Are you issuing bounties for independent work? (DAO-like)
* Are you paying in crypto? (Grant)
* Are you not always performing KYC on contributors? (Payroll)
* Are you running remote community events? (Community first)
* Are you recently funded, struggling to hire? (Early stage)

If you answer **"yes"** to **any** of the above, read on.

## Background

I remember the 2020/21 blockchain developer space. Spit on the hand and shake, push a PR, then, give a wallet address and get paid. Fifty other contributors scooped from Twitter doing the same. Fun times. Almost a cultural movement—remote, open, borderless. Just push the code. It somewhat also rode on the back of "Everyone should learn to code" and rise of the freelancer movements.

Those principles continue, even if the effectiveness of such organizations was/is questionable. The idea took root and became part of the remote work ethos. **From around 2020, someone in the North Korean Defense Ministry noticed the opportunity and shifted from low-paying Fiverr gigs to high-paying startup gigs.** Why not? Most of HR sucks at recruiting. And even if it wouldn't, the recruiting pipeline through remote channels is long, dark and full of terrors.

## Worker or Hacker?
**A DPRK IT worker is not a DPRK hacker.** <sub>*with caveats</sub>
 
Hackers are smart, aggressive, focused on exploitation, lurking in the shadows. They take a picture of the lock after disabling the CCTV. Return with a crafted lock-pick. Open the door, grab the stash, make a run.

**Workers are average (with exceptions), passive (almost no exceptions), spamming their way to success (relentlessly), in the open**. They will put on a hardhat, and you'll wave them in. They might even do some electrical work while at it, although you will need to hire a certified specialist to re-wire everything afterward.

DPRK IT worker service consists of:

1. **Defrauding the company:** The company is paying someone whose identity they do not know.
2. **Subpar operational security:** DPRK IT workers share credentials among themselves in open channels, have a poor command of Git, and unintentionally and intentionally leak granted access to third parties.
3. **Extortion:** They may try to extort more money after a job is finished.
4. **Future hacking activities:** They may use gained knowledge for future hacking activities.
5. **Sanctions violations:** North Korea is a sanctioned entity. No company can legally transfer funds to DPRK-related operations.
6. **Contribution to the North Korean Military:** DPRK IT worker salaries directly contribute to the Military Ministry of North Korea. IT workers do not keep the salaries for themselves.

As seen above, the competences of the two teams sometimes cross over. A separate article can be written on each point; it's extensive. Maybe later.

We already covered basic hints on what to look out for when it comes to the typical DPRK IT Worker profile as [part of the guide for the software we are developing for data mining on Github profiles.](https://ketman.org/malicious-github-accounts.html) Although, that was theory, now, from practice, I noticed what usually makes the "light bulb switch" for the affected project is

1. Re-evaluating social skills of the DPRK IT Worker. They're terrible, not like geek-terrible, more like, you know... living under the dictator that turned the Northern Korea into a peasant society and rules it using fear as a tool for persuasion. It makes them steer conversations toward strictly technical details.
2. Looking back at all interactions with the suspicious employee. Varying quality of work and communication on regular basis. It's hard for the DPRK handler to always allocate the same worker to the same gig, sometimes they'll "forget" what they were talking/doing yesterday, complete amnesia-style.

## Okay, It's Bad, But I'm Not Getting Hacked, Am I?

You are. **In one of the worst possible ways.** It's just not imminent and more subtle. Neither SAST, fuzzing, nor formal verification will stop it. Your experienced engineer may also get fooled, the technical output can't be used as the only evaluator. The IT world is full of eccentric personalities and DPRK worker may just seem like the another one. 

Subpar operational security (Point 2) and future hacking activities (Point 4) are at the center of the problem. Why? I'll go through a few real-life examples from the February operations.

1.  Subpar operational security:
    1.  Discovered accounts were operated by more than a single person.
    2.  Accounts hosted public repositories with multiple types of secrets leaked, including, but not limited to, wallet private keys, GitHub access tokens, private RPC endpoints or AWS API keys. **In at least a few instances, the leaked secrets were part of the previous employment gig.** Pushed now to the public repository to make the "portfolio" look better.

2.  Future hacking activities:
    1.  Affected projects were often granting `write` permissions on repositories to the DPRK IT worker. Although, in those cases, CI/CD pipelines were not present, it's possible to leverage elevated permissions into a completely fresh attack vector on software builds. **An extremely well-written walk-through on this can be found on [Adam Khan's blog](https://adnanthekhan.com/2025/02/27/not-so-safewallet-github-actions-risks-impacting-safes-frontend/).** Basically, it's easier to elevate permissions or spear phish access tokens when already invited to the organization. Another example is an adjacent observation from some scans we're running; see [my recent tweet](https://x.com/blackbigswan/status/1895099221319262257/photo/1).
    2.  Ecosystem reconnaissance. I'm a believer in the behavioral hypothesis on DPRK hackers that states, "DPRK hacks only what they know." They first use the project as users, scope out its partners and dependencies, set up the stack in the lab, maybe even send a PR. What's relevant about the hypothesis for the DPRK IT worker threat is all activity we spotted was targeted at a particular type of "ecosystem." We had a cluster of accounts focused on working in `ChainAppA`, then the other cluster focused on the work in `ChainAppB`. They were on a path to be among the most active contributors in both ecosystems. **You are effectively incubating (and paying for) hackers who won't report vulnerabilities.**
    3.  Social engineering. Trust is built slowly. It's not an obstacle for the North Korean engineer. It's actually a feature. With each PR merged, bounty paid, short exchange of messages, you lower your defenses. The first, second, and third code samples you review and run will be clean. *(Although, you'll probably [still run it in the VM](https://x.com/safe/status/1897663514975649938), right?)* **What about the *twenty-fourth* code sample? Yeah. What about your non-tech team members or the marketing team asking for a new `.ico` file design? Do they also open it in a VM?** In some past cases, affected projects required "convincing" about the DPRK IT worker's maliciousness; "everything was fine for the **last X months**."  A sort of Stockholm syndrome kicks in. A scam victim continues sending money to the scammer out of shame at admitting being fooled. And I really get it; it's hard. I don't like being fooled either.


## Postscriptum

I mostly referred to Web3 examples, that's where we operate right now and where we have the biggest successes. But we consistently find companies and projects outside of the Web3 being affected (see, [Mandiant write up that's more focused on DPRK IT Workers in the regular software world](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)). Those are somewhat even more clueless, not used as much to operating in a high-risk spaces.

Additionally, it's just the tip of the iceberg. A loose collection of thoughts on experiences from the last month where we landed in our first "war room" meetings related to the DPRK IT worker problem. I was recently asked, "How do you spot them?"—it's 50% data analysis/mining and 50% vibes at this point. I want to push the ratio more toward automation, although I already know it won't be possible to automate in 100%. So, don't expect this turning into a bullshit fix-it-all SaaS solution anytime soon and beware of people making such claim. It requires more granular approach and participation all the way from the bottom of the software world - security engineers, engineers, communities, projects and even government. We will continue to be the pain in the ass for *the DPRK boys* though.

And, my plea to you, your project, and your investors is:

**Treat this seriously.** 

**Don't hire off the street. If something's off about the hire, stop and think.**

**Answer when we write to you in a reasonable time frame.**

**Verify what we are signaling to you. (It's free)**

I'll write about some "bloopers" next time. Yes, we get those too with our overly-friendly yet not-that-talkative Korean peninsula friends.