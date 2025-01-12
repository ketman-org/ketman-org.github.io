---
title: Malicious Github Accounts with gh-fake-analyzer
date: 2024-11-01
categories:
  - Software
  - DPRK
image: article-image.png
authors: [blackbigswan]
# featured: true
excerpt: On classifying GitHub profiles as potentially malicious using gh-fake-analyzer.
---

# Malicious Github Accounts

See [INVESTIGATIONS](https://github.com/shortdoom/gh-fake-analyzer/tree/main/profiles/INVESTIGATIONS) for some high-confidence accounts dumped using `gh-analyze` tool.

Additionally, here's the list of past investigations done with `gh-fake-analyzer`.

[Network of Fake Recruiter and Developer Accounts Linked to Lazarus](https://medium.com/@-Heiner/cc361074bdc2)

[Lazarus patterns discovered with gh-fake-analyzer](https://github.com/BlockOSINT/-threat-research-and-intelligence-/blob/main/Investigations/suspicious-activity-on-github/North-Korea-sponsored-APT/lazarus-group.md)


**Disclaimer:**  The confidence in detecting "malicious" GitHub profiles is low. Many regular user accounts may appear in the analysis files; this does not indicate their participation in any illegal activity. ANYBODY can edit the `.git` file, and ANYBODY can commit code to GitHub. This tool is intended for reconnaissance purposes only. The information provided here **may** be incorrect. Please do not make any (baseless) accusations based on this content. All information is sourced from publicly available third-party sources and verified to the best of my ability (only).

It's possible, to a certain degree, to define some metrics for classifying GitHub profiles as potentially malicious. However, motivated enough attackers can still bypass most of those checks and appear as professional engineers. If that's the case, a company should fall back to regular methods of judging a potential employee/contact. The `gh-analyze` can help out with finding some dark patterns if the attacker is not motivated enough :)

1. Does any (not forked) repository or commit predate the account creation date? If yes - suspicious.
    - inspect the repository and search on github for similar repositories. it's potentially a copy of other repository
    - non-malicious cases are: rebasing, transfering .git repo between the accounts etc.
2. Does any (not forked) repository have more contributors than the owner? If yes - check contributors;
    - is contributor profile suspicious? check contributors profiles themselves.
    - are contributor contributions meaningful or low-effort all across?
3. How many unique emails do you find in commit messages?
    - non-malicious for fully legitimate accounts
    - can be malicious if you recognize a pattern of:
        - trying to hide the (owner's) identity, changing the identity often, using address/name attached to different person
4. Does any commit message appear copied from another repository? 
    - you need to run `--commit_filter` and inspect `matching_repos` number, look for *unique* commit messages
    - merge commit messages, if copied, often preserve the original owner's nickname
5. While getting "all repositories" for an onwer account, do some repositories return an error with DMCA takedown?
    - non-malicious for fully legitimate accounts
    - DMCA takedowns, deleted repositories and empty repositories, if existing together on the account, may suggest some automation software usage
6. Issue-spamming on high-credibility organizations. Some accounts were collecting "github badges" using this method. After opening an issue on, for example, Ethereum organization, the organization "badge" will be visible on main profile page and account will be credited as a "contributor" to Ethereum organization.
    - do not trust Activity Overview badges blindly, use report files from `gh-analyze` to check the actual commit (if there's any)
7. Look "around" the account, not only on the account. Followers/Following patterns are often a tell-tale.

Great list of (non-technical) flags by ZachXBT: https://x.com/zachxbt/status/1824047480121729425

Some indicators teams can look out for in the future includes:

1. They refer each other for roles
2. Good looking resumes / GitHub activity although sometimes lie about work history.
3. Typically are happy to KYC but submit fake IDs in hopes teams do not investigate further
4. Ask specific questions about locations they claim to be from.
5. Dev is fired and immediately new accounts appear looking for work
6. May be good devs initially but typically start to underperform
7. Review logs
8. Like using popular NFT pfps
9. Asia accent

# Regular, Skid/MaaS and DPRK-style profile

Heuristics here is only informational. There can be a lot of edge cases, false positives and false negatives both happen and are hard to deduce from report files, the following are nothing else than a list of rules-of-thumb. See "External Sources" for attribution details.

*PS. Analysis files follow still the old `gh-analyze` report format.*

### Features of regular accounts

1. No commits before the account creation date
2. Contributors (to the owner's repositories) are none/small amount and if there are any, the contributor profile itself is not suspicious
3. Little amount of unique mails in commit messages, no often identity changes
4. No commit messages copied
5. No DMCA takedowns
6. At least some repositories contain "original" code
7. Non-toxic following/follower patterns, mutual following is present
8. Legit contributors to owner's code

### Features of Skid/Malware-as-a-service accounts

For Skid accounts - Example: eduales99 and sebastian4098

1. Commits before the creation date of acount (all eduales99 repositories)
2. Weird contribution from sebastian4098 to a single repo, sebastian4098 itself is a suspicious account
3. Weird non-owner emails as authors/contributors to owner repositories, indicates many accounts used for setting up/boosting credibility of this profile
4. Copied commit messages from real repository
5. DMCA takedown on a repository (mirrored real repository)

So-called "Farmed accounts". Farms themselves only run those accounts in an automatic way, breadcrumbs to follow are everywhere. Further modeling would probably unearth some dark patterns of such clusters. The best bet is to inspect follower/following pattern and quality of repositories. Farmed accounts usually won't host any original code, a lot of tutorial-level code and overcompensate on profile's README page.

**External Sources:**

[Contagious Interview](https://github.com/tayvano/lazarus-bluenoroff-research?tab=readme-ov-file#%EF%B8%8F-contagious-interview)

### Features of DPRK-style accounts

For DPRK-style - Example: light-fury, 0xm00neth, bluesky0309

1. No commits before the account creation date. Probably an old stolen GitHub account (for light-fury we can find sergeypt423 that made the first commit to this account in 2017, points to Kenyan freelancer forum). Time series analysis of commits is useful, are there any significant leaps in the activity? 
2. Weird contributions by many accounts to some fairly big projects like GaimzWeb/Mobile, but this is not neccessarily a red flag, regular accounts can be similar, however, project itself seem suspicious.
3. A ton of different emails in commit messages. A strong cluster of many accounts "working together" to boost light-fury's credibility. It's consistent with a pattern of "recommending a friend for a work"
4. No commit messages copied

Very hard to distinguish from the regular account, but there are some flags. Analyzing clusters of activity on such account and checking the merit of their work is basically the only way to distinguish DPRK-style hacker from a regular account. Light-fury was commiting working code to multiple legit organizations at the acceptable level of effort (Whitelisting is therefore not very efficient), same as 0xm00neth and bluesky0309, however, those users were far less careful with building up the history of their accounts and we can spot copied repositories for bluesky0309, sometimes with exact merge messages of the original repository. 

**External Sources:**

[Light-fury cluster discussion](https://x.com/tayvano_/status/1824257014639497366)

[0xm00neth cluster discussion](https://x.com/blackbigswan/status/1825247425574863176)