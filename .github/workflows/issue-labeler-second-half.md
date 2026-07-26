---
timeout-minutes: 5

on:
  workflow_dispatch:
    inputs:
      issue_context:
        description: 'Context of the issue that the workflow should label'
        required: true
        type: string
  # issues:
  #   types: [opened]
  # roles: all

permissions:
  issues: read
  contents: read
  copilot-requests: write
tools:
  github:
    toolsets: [issues, labels, repos]
    lockdown: false

safe-outputs:
  add-labels:
    allowed: [ext-testlib, fastmodel, gdb, github, good-first-contribution, gpu, gpu-compute, help wanted, learning-gem5, mem, mem-cache, mem-garnet, mem-ruby, misc, python, question, resources, resources-website, scons, sim, sim-se, stats, stdlib, systemc, tests, util, util-docker, util-gem5art, util-m5, website]
    # invalid, low-priority, needs details, Stale, system-arm, and wontfix excluded from this list
  add-comment: {}
  noop:
    report-as-issue: false

engine:
  id: copilot
  env:
    COPILOT_PROVIDER_BASE_URL: https://api.openai.com/v1
    COPILOT_MODEL: gpt-5-mini
    COPILOT_PROVIDER_API_KEY: ${{ secrets.COPILOT_PROVIDER_API_KEY }}


---

# Issue Labeler - Second Half

Print the following message to the Agentic Conversation:

`Using the issue labeler workflow file, second half, from the stable branch`

Next, call the noop tool and exit.
