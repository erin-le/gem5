---
description: Investigates failed test workflows to identify root causes and patterns and rerun if the failure isn't related to the code
on:
  workflow_dispatch:

  workflow_run:
    workflows: ["Daily Tests", "Weekly Tests", "Compiler Tests", "CI Tests"]
    types: [completed]

  bots: ["github-actions[bot]"]
  roles: all
# Only trigger for failures - check in the workflow body
# The condition after the &&: Don't run the Test Failure Doctor if the triggering
# workflow is on its 2nd run/1st rerun (or greater). This is to try to save tokens.

if: ${{ (github.event.workflow_run.conclusion == 'failure' || github.event.workflow_run.conclusion == 'timed_out') && !(github.event.workflow_run.run_attempt > 1) }}

permissions: read-all

network: defaults

safe-outputs:
  create-issue:
    title-prefix: "misc: [Test Failure Doctor] "
  add-comment:
  update-issue:
  noop:
  jobs:
    rerun-failed-jobs:
      permissions:
        actions: write    # this permission is needed to rerun failed jobs
      description: "Rerun failed jobs for a given workflow run ID."
      steps:
        - name: Rerun failed jobs
          uses: actions/github-script@v8
          env:
            RUN_ID: ${{ github.event.workflow_run.id }}
          with:
             script: |
                await github.rest.actions.reRunWorkflowFailedJobs({
                   owner: context.repo.owner,
                   repo: context.repo.repo,
                   run_id: parseInt(process.env.RUN_ID, 10)
                });

tools:
  github:
    # `default` expands to context, repos, issues, pull_requests and users;
    # `actions` allows for access to workflow logs and artifacts
    toolsets: [default, actions]
    lockdown: false
timeout-minutes: 20

engine:
  id: copilot
  env:
    COPILOT_PROVIDER_BASE_URL: https://api.openai.com/v1
    COPILOT_MODEL: gpt-5-mini
    COPILOT_PROVIDER_API_KEY: ${{ secrets.COPILOT_PROVIDER_API_KEY }}

---
# Test Failure Doctor

Print the following message to the Agentic Conversation:

`Using the test failure doctor workflow file from the stable branch`

Next, call the noop tool and exit.
