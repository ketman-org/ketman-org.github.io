---
title: Introducing Ketman Project
date: 2024-11-01
categories:
  - Software
  - Investigation
author: Ketman
image: another-image.png
featured: true
excerpt: In the ever-evolving landscape of cybersecurity, traditional methods of tracking threat actors through hashes, IPs, and websites are not enough. Today...
---

# Introducing Ketman Project: A Novel Approach to Threat Actor Detection

The cybersecurity world has a blind spot, and it's a big one. While we've gotten pretty good at spotting malware and blocking suspicious IPs, there's a much more insidious threat that's been flying under the radar: so-called **"fake developers"** who play the long game, sometimes spending significant time and effort building their cover before striking. These sleeper agents are often part of well-organized and technically sophisticated groups - including **North Korean-sponsored** APTs. From our more confident attributions, we can observe a new pattern of threat actors: instead of tedious spear-phishing attacks or time-consuming reconnaissance of carefully hidden technical aspects of company infrastructure, they choose a more "upstream" route. They either **hire themselves at your company and inject malicious code as part of the day-to-day** routine, **or they attack the software vendors you already trust**.

The landscape of cyber threats has evolved beyond traditional attack vectors, with threat actors increasingly exploiting trust mechanisms within development ecosystems. The emergence of investigations into **DPRK IT workers** has highlighted a critical gap in conventional threat intelligence approaches, particularly in **addressing insider threats and supply chain attacks**.

Ketman isn't just a set of tools - it's an active investigation and monitoring platform that provides unprecedented context around threat actors. By combining our in-house tooling with continuous threat monitoring, we maintain an ever-growing database of threat actor profiles, campaign attributions, and evolving attack methodologies. This collaborative approach allows us to map relationships between seemingly disparate campaigns and actors, providing a broader understanding of the threat landscape.

### Comparative Analysis of Threat Vectors Covered by Ketman

The Spear Phishing Malware column is used for comparison to Ketman's covered attack vectors:

| Characteristic        | Fake Developer / Insider Threat               | Supply Chain Attack                    | Spear Phishing Malware          |
| --------------------- | --------------------------------------------- | -------------------------------------- | ------------------------------- |
| Duration              | Medium to long-term                           | Variable                               | Variable                        |
| Digital Footprint     | Established presence / Fabricated legitimacy  | Source Code / Network data             | Network data                    |
| Detection Difficulty  | Medium/Very High                              | High/Easy                              | Variable                        |
| Attack Surface        | Internal systems / Open source / Hiring       | Open source / Vendors / Infrastructure | Direct payload delivery         |
| Trust Exploitation    | HR / Business / Engineering                   | Engineering                            | All company                     |
| Attribution Challenge | Identity verification / Behavioral signatures | Many different agents (non-APT)        | Many different agents (non-APT) |
| Impact Severity       | High                                          | High                                   | Variable                        |
| Recovery Complexity   | High                                          | High                                   | Variable                        |

For Fake Developer campaigns, we define that:

1. Modern threat actors maintain a persistent presence across multiple platforms
2. Digital behaviors create unique, difficult-to-fake patterns
3. Cross-platform correlation provides richer attribution data
4. Automated analysis can scale pattern detection
5. Past data provides clues for future behavior

Ketman's supply chain threat intelligence solution is currently in early development, but we have already concluded:

1. Supply chain attacks are similar to Fake Developer attacks, only reversed in dynamics
2. A fake developer can turn your company into part of a supply chain attack, especially if you are a software vendor
3. Supply chain attacks can be mitigated confidently, and the data can be used to further build up the actors database

### Leveraging Web3-related Footprints

The public nature of Web3 ecosystems provides unique opportunities for threat intelligence gathering. Unlike traditional cyber attacks potentially involving state actors (e.g., the Bangladesh SWIFT hack), the same actors (e.g., DPRK IT Workers) operating in the Web3 ecosystem must maintain a more public profile (See: Contagious Interview), thus creating more extensive digital footprints for analysis. The personal nature and often long-term duration of operations provides more unique data for modeling. We expect further evolution of the "Fake hire" attack vector, as it remains effective and threat actors display adaptation.

## Ketman and The Power of Pattern Recognition

At its core, Ketman specializes in uncovering threat actors through behavioral patterns across the open-source ecosystem. We currently focus on GitHub, where our analysis encompasses:

- Repository activity patterns
- Contribution behaviors
- Profile information and BIOs
- Image analysis
- Follow/following relationships
- Code commit patterns
- Package publication patterns
- Cross-platform identity correlation
- Source code analysis across hosting platforms

We have collected and labeled the most comprehensive dataset of threat actors active in the open source ecosystem. Our investigative methodology works around eight principles:

1. Initial broad-spectrum data collection
2. Dataset schema design
3. Pattern identification and clustering
4. Cross-platform correlation
5. Behavioral profile development
6. Attribution framework application
7. Dataset schema optimization
8. Publication - context-based investigation and data

### Advanced Search Capabilities with KetmanSearch

We are running a private search engine platform. The platform implements a search-centric design philosophy, making it accessible to both technical and non-technical researchers. Our search engine offers:

- Flexible faceted filtering
- Granular search controls
- Results summarization
- Image search capabilities
- Data pinning interface for investigation tracking
- Easy to navigate data schema
- Access to all past and current data

## Focus Areas

### Fake Developer Profiles

Ketman's approach flips the script. Instead of looking for technical indicators that might not exist, it looks for the one thing these actors can't hide: their patterns of behavior. Every fake account, every manufactured contribution, and every attempted relationship-building exercise leaves traces. When you know what to look for, these traces form patterns that are surprisingly hard to hide.

- Credential boosting attempts
- Identity masking and impersonation
- Malware distribution networks

The goal isn't just to catch threats – it's to make it so difficult and expensive to maintain fake personas that the attack method becomes impractical.

### Open Source Attack Patterns

- Supply chain attacks targeting package managers (npm/pip) and other upstream software
- Suspicious contributions (Insider Threat) and toxic pull requests

### Proactive Defense

- Early identification of suspicious behavior patterns
- Attribution of seemingly unrelated activities to actor clusters
- Predictive analysis of potential threats
- Real-time monitoring of evolving attack methodologies

## The Ketman Ecosystem

We are building a comprehensive suite of tools for threat intelligence and actor detection:

- `gh_fake_analyzer`: An open-source package for suspicious GitHub profiles dataset generation and analysis
- Ketman Investigation Portal: Real-time analysis of past and ongoing malicious campaigns
- The Ketman Dataset: A continuously updated, labeled dataset of threat actors and their activities
- Other custom tooling for data collection and pattern analysis across the open-source ecosystem

# Conclusion

The threat landscape has fundamentally shifted from traditional attack vectors to more sophisticated, long-term infiltration strategies. As threat actors continue to evolve their tactics, particularly in exploiting trust within the open-source ecosystem, traditional security measures alone are no longer sufficient By combining advanced pattern recognition, comprehensive data collection, and innovative analysis techniques, we're not just detecting threats – we're making it increasingly difficult for malicious actors to maintain their cover. Our approach turns their greatest strength – the need for long-term presence – into a vulnerability that can be detected and tracked.
