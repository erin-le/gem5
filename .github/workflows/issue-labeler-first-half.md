---
timeout-minutes: 5

on:
  workflow_dispatch:
    inputs:
      issue_id:
        description: 'Issue id'
        required: true
        type: string
      issue_title:
        description: 'Issue title'
        required: true
        type: string
      issue_body:
        description: 'Issue body'
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
    allowed: [arch, arch-arm, arch-gcn3, arch-mips, arch-power, arch-riscv, arch-sparc, arch-vega, arch-x86, base, base-stats, bug, build error, classic caches, compilation error, configs, cpu, cpu base, cpu-kvm, cpu-minor, cpu-o3, cpu-simple, dependencies, dev, dev-arm, dev-hsa, dev-virtio, doc, dram, duplicate, enhancement, ext]
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

# Issue Labeler - First Half

Print the following message to the Agentic Conversation:

`Using the issue labeler workflow file, first half, from the stable branch`

Next, call the noop tool and exit.
