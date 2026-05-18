---
description: |
  This workflow creates weekly repo status reports. It gathers recent repository
  activity (issues, PRs, discussions, releases, code changes) and generates
  engaging GitHub issues with productivity insights, community highlights,
  and project recommendations.

on:
  # schedule: weekly
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
  #staged: true
  mentions: false
  allowed-github-references: []
  create-issue:
    title-prefix: "misc: "
    labels: [misc]
    close-older-issues: true
  report-failure-as-issue: false
source: githubnext/agentics/workflows/daily-repo-status.md@410f8f4fdfbd7d855fc58c2df6438d2ebfa7c93e
engine: copilot
---

# Weekly Repo Status

Create an weekly status report for the gem5/gem5 repo as a GitHub issue.
When "weekly" or "in the last week" is used, and the workflow was automatically launched (i.e. triggered by scheduler.yaml), it specifically refers to the time since the last automated run of this workflow. If this workflow was launched by a GitHub user, you should include all activity starting from exactly a week before the workflow was launched.

For example, if this workflow is run at May 18th at 9pm, then the summary should include all activity between May 11th at 9pm and May 18th at 9pm.

## What to include

- An executive summary of what has been done in the last week.

- A list of PRs and issues that were opened in the last week, and a short summary of each. This list should be formatted as a table with the PR number, title, author, and summary. Key words and phrases in the summary should be bolded. Use the table template shown below:

| PR | Title | Author | Summary |
|----|-------|--------|---------|

- A list of PRs and issues that were modified in the last week, and a short summary of what the changes were. This list should also be formatted as a table with the PR number, title, author, and summary. Key words and phrases in the summary should be bolded. The summary for a PR should not include activity from previous runs of this workflow that mention the PR. The summaries also should not mention runs of CI tests for the PR, unless there were test failures.
Use the table template shown below:

| PR | Title | Author | Summary |
|----|-------|--------|---------|

- A list of PRs that haven't had any activity in the last two weeks. This list should have the PR number, title, name of the author, a summary of the changes made, and the status of the PR, e.g. if it's been waiting for a response from the author or reviewer for two weeks or more, if two weeks or more have passed with no activity since the PR was opened, etc. The summary for a PR should not include activity from previous runs of this workflow that mention the PR.
Split this list into two parts. The first should be for PRs that haven't had activity in approximately two weeks, the second should be for PRs that haven't had activity for longer periods of time.
This list should be formatted as follows:

| PR | Title | Author | Summary | Status |
|----|-------|--------|---------|--------|

- A list of issues and PRs that might be high priority.
  - An issue might be high priority if:
    - several community members have commented on it and said that they have encountered the same issue, especially if the issue causes the simulation to crash or produce inaccurate results.
    - One of the gem5 developers was pinged on the issue. The GitHub usernames of the gem5 developers are `BobbyRBruce`, `Harshil2107`, `erin-le`, and `powerjg`.

  - A PR might be high priority if:
    - One of the gem5 developers has been pushing commits to it. The GitHub usernames of the gem5 developers are as follows: `erin-le`, `Harshil2107`, `BobbyRBruce`, `powerjg`.
    - If the PR has been marked for inclusion in the next release
    - If the PR is a fix for a high priority issue
    - One of the gem5 developers was pinged on the PR. The GitHub usernames of the gem5 developers are as follows: `erin-le`, `Harshil2107`, `BobbyRBruce`, `powerjg`.
  - Organize this list so all of the PRs are listed, then all of the issues. Use the following format:
| PR | Title | Author | Why High Priority | Actions Needed |
|----|-------|--------|-------------------|----------------|

- A list of actionable next steps for PRs and issues, split up by gem5 developer. The list should be formatted as follows:
| PR | Title | Author | gem5 Developer | Actions Needed |
|----|-------|--------|----------------|----------------|

## Style

- The title of the summary issue should consist of the title prefix, `misc: `, followed by the following format:
`Weekly Repo Status: {month} {start_day} - {month} {end_day}, {year}`, where the words enclosed in curly brackets should be swapped out for the appropriate days, months, and year. For example, if this workflow is run on May 18th, 2026, then it will contain activity starting from May 11th, so the title should be `Weekly Repo Status: May 11 - May 18, 2026`.
- Be concise - adjust length based on actual activity
- Be positive, encouraging, and helpful
- Bold key words in summaries of issues/PRs

## Process

1. Gather recent activity from the repository
2. Study the repository, its issues and its pull requests
3. Create a new GitHub issue with your findings and insights
