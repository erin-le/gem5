---
description: |
  This workflow creates weekly repo status reports. It gathers recent repository
  activity (issues, PRs, discussions, code changes) and generates a summary GitHub issue.

on:
  workflow_dispatch:

permissions:
  contents: read
  issues: read
  pull-requests: read
  discussions: read
  copilot-requests: write

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
    title-prefix: "misc: "
    labels: [misc]
    close-older-issues: true
  report-failure-as-issue: false

engine:
  id: copilot
  env:
    COPILOT_PROVIDER_BASE_URL: https://api.openai.com/v1
    COPILOT_MODEL: gpt-5.4
    COPILOT_PROVIDER_API_KEY: ${{ secrets.COPILOT_PROVIDER_API_KEY }}

---

# Weekly Repo Status

Create a weekly status report for the gem5/gem5 repo as a GitHub issue.
When "weekly" or "in the last week" is used, and the workflow was automatically launched (i.e. triggered by scheduler.yaml), it specifically refers to the time since the last automated run of this workflow. If this workflow was launched by a GitHub user, you should include all activity starting from exactly a week before the workflow was launched.

For example, if this workflow is run at May 18th at 9pm, then the summary should include all activity between May 11th at 9pm and May 18th at 9pm.

- In the section below, the words "item" or "items" refers to PRs, issues, and discussions.

## What to include

- An executive summary of what has been done in the last week.

- Lists of PRs, issues, and discussions that were opened in the last week, and a short summary of each. Only include items that are still open. PRs, issues, and discussions should be sorted into separate lists, and within each list, items should be sorted from newest to oldest, i.e. by descending PR/issue/discussion number. These lists should be formatted as tables with the PR/issue/discussion number, title, author, and summary. Key words and phrases in the summary should be bolded. Use the table template shown below:

| # | Title | Author | Summary |
|---|-------|--------|---------|

- Lists of PRs, issues, and discussions that were modified, had new comments added, or had other activity in the last week. Provide a short summary of what the changes were, and/or what the activity was. The PRs, issues, and discussions in this section should be as though you filtered them by the `updated` qualifier between the current time and a week ago, and excluded the ones that were `created` between the current time and a week ago.

There should be two lists in total. The first should contain items that were created in the last 2-6 weeks, and the second should contain items created over 6 weeks ago. Pay special attention to older, formerly inactive items that had recent activity.

Within each table, items should first be sorted by whether they are PRs, issues, or discussions, then sorted in order of descending PR/issue/discussion number. Key words and phrases in the summary should be bolded, and the summary itself should be kept concise. The summary should not include activity from previous runs of this workflow that mention the PR/issue/discussion. The summaries also should not mention runs of CI tests for PRs, unless there were test failures.


These lists should also be formatted as tables with the PR/issue/discussion number (in the `| # |` column), whether the item is a PR/issue/discussion (in the `| Type |` column), the title, author, person/people who updated, and summary. The PR/issue/discussion number should link to the PR/issue/discussion.

| # | Type | Title | Author | Updated by | Summary |
|---|------|-------|--------|------------|---------|

- A list of PRs that were last updated in the last six weeks, but haven't had any activity in the last two weeks. This list should have the PR number, title, name of the author, a summary of the changes made, and the status of the PR, e.g. if it's been waiting for a response from the author or reviewer for two weeks or more, if two weeks or more have passed with no activity since the PR was opened, etc. The summary for a PR should not include activity from previous runs of this workflow that mention the PR. Sort PRs by descending order of PR number.
This list should be formatted as follows:

| PR # | Title | Author | Summary | Status |
|------|-------|--------|---------|--------|

In the `Status` section, include *what the last activity was*, *who the last activity was from* and *how long it has been since the last activity*.


- A list of issues, PRs, and discussions that might be high priority.
  - An issue might be high priority if:
    - several community members have commented on it and said that they have encountered the same issue, especially if the issue causes the simulation to crash or produce inaccurate results.
    - One of the gem5 developers was pinged on the issue. The GitHub usernames of the gem5 developers are `BobbyRBruce`, `Harshil2107`, `erin-le`, and `powerjg`.

  - A PR might be high priority if:
    - One of the gem5 developers has been pushing commits to it. The GitHub usernames of the gem5 developers are as follows: `erin-le`, `Harshil2107`, `BobbyRBruce`, `powerjg`.
    - If the PR has been marked for inclusion in the next release
    - If the PR is a fix for a high priority issue
    - One of the gem5 developers was pinged on the PR. The GitHub usernames of the gem5 developers are as follows: `erin-le`, `Harshil2107`, `BobbyRBruce`, `powerjg`.

  - A discussion might be high priority if:
    - several community members have commented on the discussion
    - One of the gem5 developers was pinged on the discussion. The GitHub usernames of the gem5 developers are `BobbyRBruce`, `Harshil2107`, `erin-le`, and `powerjg`.

  - Organize this list so items are grouped by whether they're PRs, issues, or discussions. Within each group, sort items in descending order of PR/issue/discussion number. Use the table template shown below:

| # | Type | Title | Author | Why High Priority | Actions Needed |
|---|------|-------|--------|-------------------|----------------|

## Style

- The title of the summary issue should use the following format:
`Weekly Repo Status: {month} {start_day} - {month} {end_day}, {year}`, where the words enclosed in curly brackets should be swapped out for the appropriate days, months, and year. For example, if this workflow is run on May 18th, 2026, then it will contain activity starting from May 11th, so the title should be `Weekly Repo Status: May 11 - May 18, 2026`.
- Be concise - adjust length based on actual activity
- Be positive, encouraging, and helpful
- Bold key words in summaries of issues/PRs

## Process

1. Gather recent activity from the repository
2. Study the repository and its issues, pull requests, and discussions.
3. Create a new GitHub issue with your findings and insights
