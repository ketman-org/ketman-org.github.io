---
title: Introducing Ketman Search Project
date: 2024-11-01
categories: 
    - Software
    - Investigation
author: Ketman
image: another-image.png
featured: true
excerpt: 
    In the ever-evolving landscape of cybersecurity, traditional methods of tracking threat actors through hashes, IPs, and websites have shown their limitations. Today...
---

# Introducing Ketman Search: A Novel Approach to Threat Actor Detection

In the ever-evolving landscape of cybersecurity, traditional methods of tracking threat actors through hashes, IPs, and websites have shown their limitations. Today, we're excited to introduce Ketman Search - a groundbreaking OSINT tool that takes a different approach to threat actor detection and investigation.

## The Power of Pattern Recognition

Unlike conventional threat intelligence platforms that focus primarily on technical indicators, Ketman Search specializes in uncovering threat actors through their behavioral patterns on GitHub. Our platform analyzes various aspects of GitHub profiles and activities, including:

- Repository activity patterns
- Contribution behaviors
- Profile information and BIOs
- Image analysis
- Follow/following relationships
- Code commit patterns

## Core Features

### Advanced Search Capabilities
At the heart of Ketman Search lies a powerful search engine designed specifically for threat intelligence. The platform prioritizes search functionality over complex dashboards, offering:

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

Beyond the search platform, the Ketman team is building a comprehensive suite of tools:

- `gh_fake_analyzer`: An open-source package for GitHub profile dataset generation
- Active investigations portal for contextual analysis
- Labeled actor profiles database

### Future Developments

Our roadmap includes:

- GitHub Action for new contributor verification
- Static analysis tools for hidden payload detection
- Active monitoring and alerting system
- Enhanced data visualization and graphing capabilities

## Why Search-Centric Design?

While many OSINT platforms focus on graph-based visualizations, we've chosen to center our platform around search functionality. This decision allows for:

- More flexible investigation patterns
- Faster iteration on theories
- Better handling of large-scale datasets
- User-driven data modeling
- Simplified but powerful interface

## Conclusion

Ketman Search represents a paradigm shift in threat actor detection, moving beyond traditional indicators to focus on behavioral patterns and platform-specific activities. By building around a powerful search core rather than complex visualizations, we've created a tool that adapts to investigators' needs while maintaining the ability to uncover complex threat actor networks.

For security teams looking to enhance their threat detection capabilities, Ketman Search offers a fresh perspective on OSINT investigations, backed by comprehensive datasets and powerful search capabilities.