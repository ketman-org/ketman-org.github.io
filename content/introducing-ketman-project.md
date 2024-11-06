---
title: Introducing Ketman Project
date: 2024-11-01
categories: 
    - Software
    - Investigation
author: Ketman
image: another-image.png
featured: true
excerpt: 
    In the ever-evolving landscape of cybersecurity, traditional methods of tracking threat actors through hashes, IPs, and websites are not enough. Today...
---

# Introducing Ketman Project: A Novel Approach to Threat Actor Detection

In the ever-evolving landscape of cybersecurity, the challenge of tracking and identifying threat actors continues to grow in complexity. While traditional indicators like hashes, IPs, and website tracking remain crucial components of threat intelligence, today we're excited to introduce Ketman Project - a comprehensive platform that combines these traditional methods with advanced behavioral analysis to build detailed threat actor profiles and attribution frameworks.

## The Ketman Investigation Platform

Ketman isn't just a set of tools - it's an active investigation and monitoring platform that provides unprecedented context around threat actors. By combining our in-house tooling with continuous threat monitoring, we maintain an ever-growing database of threat actor profiles, campaign attributions, and evolving attack methodologies. This collaborative approach allows us to map relationships between seemingly disparate campaigns and actors, providing a broader understanding of the threat landscape.

## The Power of Pattern Recognition

At its core, Ketman specializes in uncovering threat actors through behavioral patterns across the open-source ecosystem. While we currently focus on GitHub, our platform is designed to analyze patterns across all major package repositories (npm, pip) and various code hosting platforms. Our analysis encompasses:

- Repository activity patterns
- Contribution behaviors
- Profile information and BIOs
- Image analysis
- Follow/following relationships
- Code commit patterns
- Package publication patterns
- Cross-platform identity correlation
- Source code analysis across hosting platforms

## Core Features

### Advanced Search Capabilities

Ketman prioritizes intuitive search functionality over complex dashboards, making it accessible to both technical and non-technical researchers. Our search engine offers:

- Flexible faceted filtering
- Granular search controls
- Results summarization
- Image search capabilities
- Data pinning interface for investigation tracking

### Practical Investigation Example

Let's walk through a real investigation pattern using Ketman Search:

1. Start with a broad search for a target profile (e.g., "FinalGoal231")
2. Refine results using the "Search In" sidebar filters:
   - Focus on specific activity types (commits, pull requests)
   - Filter by repository count (e.g., >10 repositories)
3. Analyze the refined results to uncover connected accounts and activities

This methodology has proven particularly effective in identifying networks of related threat actors and their activities.

## Focus Areas

Ketman Search specializes in detecting:

### Fake Developer Profiles
- Credential boosting attempts
- Identity masking and impersonation
- Malware distribution networks

### Open Source Attack Patterns
- Supply chain attacks targeting package managers (npm/pip)
- Source code execution payload injection
- Suspicious contributions and toxic pull requests

### Proactive Defense
- Early detection of actor clusters
- Pattern-based threat prediction
- Active monitoring of suspicious activities

## The Ketman Ecosystem

We are building a comprehensive suite of tools for threat inteligence and actor detection.

- `gh_fake_analyzer`: An open-source package for suspicious GitHub profiles dataset generation and analysis
- Ketman Investigation Portal: Real-time analysis of past and ongoing malicious campaigns
- The Ketman Dataset: A continuously updated, labeled dataset of threat actors and their activities
- Other custom tooling for data collection and pattern analysis across the open-source ecosystem

## Why Search-Centric Design?

While many OSINT platforms focus on graph-based visualizations, we've chosen to center our platform around search functionality. This decision allows for:

- More flexible investigation patterns
- Faster iteration on theories
- Better handling of large-scale datasets
- User-driven data modeling
- Simplified but powerful interface

## Conclusion

Ketman Search represents a paradigm shift in threat actor detection, focusing on behavioral patterns and platform-specific activities. By building around a powerful search core rather than complex visualizations, we've created a tool that adapts to investigators' needs while maintaining the ability to uncover complex threat actor networks.

For security teams looking to enhance their threat detection capabilities, Ketman Search offers a fresh perspective on OSINT investigations, backed by comprehensive datasets and powerful search capabilities.