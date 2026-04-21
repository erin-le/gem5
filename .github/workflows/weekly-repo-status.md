---
description: |
  This workflow creates weekly repo status reports. It gathers recent repository
  activity (issues, PRs, discussions, releases, code changes) and generates
  engaging GitHub issues with productivity insights, community highlights,
  and project recommendations.

on:
  schedule: weekly
  workflow_dispatch:

permissions:
  contents: read
  issues: read
  pull-requests: read

network: defaults

tools:
  github:
    # If in a public repo, setting `lockdown: false` allows
    # reading issues, pull requests and comments from 3rd-parties
    # If in a private repo this has no particular effect.
    lockdown: false
    min-integrity: none # This workflow is allowed to examine and comment on any issues

safe-outputs:
  mentions: false
  allowed-github-references: []
  create-issue:
    title-prefix: "[repo-status] "
    labels: [report, weekly-status]
    close-older-issues: true
  report-failure-as-issue: false
source: githubnext/agentics/workflows/daily-repo-status.md@410f8f4fdfbd7d855fc58c2df6438d2ebfa7c93e
engine: copilot
---

# Weekly Repo Status

Create an weekly status report for the repo as a GitHub issue.

## What to include

- A list of PRs and issues that were opened in the last week, and a short summary of each. This list should be formatted as a table with the PR number, title, author, and summary. Key words and phrases in the summary should be bolded. Use the table template shown below:

| PR | Title | Author | Summary |
|----|-------|--------|---------|

- A list of PRs and issues that were modified in the last week, and a short summary of what the changes were. This list should also be formatted as a table with the PR number, title, author, and summary. Key words and phrases in the summary should be bolded. Use the table template shown below:

| PR | Title | Author | Summary |
|----|-------|--------|---------|

- Lists of PRs that haven't had any activity in the last two weeks. One list should be PRs that are waiting for a specific reviewer's response, the other list should be PRs that are waiting for the author's response, and the last list should be PRs that haven't had any activity after being opened and need an initial review.

  - These lists should be formatted as follows:

  ### Awaiting reviewer's response
  | PR | Title | Reviewer | Summary |
  |----|-------|----------|---------|

  ### Awaiting author's response
  | PR | Title | Author | Summary |
  |----|-------|--------|---------|

  ### Awaiting initial review
  | PR | Title | Author | Summary |
  |----|-------|--------|---------|


- A list of issues and PRs that might be high priority.
  - An issue might be high priority if:
    - a number of community members have commented on it and said that they have encountered the same issue
    - One of the gem5 developers was pinged on the issue.

  - A PR might be high priority if:
    - One of the gem5 developers has been pushing commits to it. The GitHub usernames of the gem5 developers are as follows: erin-le, Harshil2107, BobbyRBruce, powerjg
  - Organize this list so all of the PRs are listed, then all of the issues.

- A list of actionable next steps for PRs and issues, split up by gem5 developer. The list should be formatted as follows:
| PR | Title | Author | gem5 Developer | Actions Needed |
|----|-------|--------|----------------|----------------|

## Style

- Be concise - adjust length based on actual activity
- Be positive, encouraging, and helpful
- Bold key words in summaries of issues/PRs

## Process

1. Gather recent activity from the repository
2. Study the repository, its issues and its pull requests
3. Create a new GitHub issue with your findings and insights
