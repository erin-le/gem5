---
timeout-minutes: 5

on:
  issues:
    types: [opened]
  pull_request:
    types: [opened]

  # workflow_call:
  # inputs:
  #   pr_issue_number:
  #     description: "PR or Issue number passed from the parent"
  #     required: true
  #     type: string

    # workflows: ["Auto Label Agent - First Half"]
    # types:
    #   - completed


# on:
#   schedule: daily
#   workflow_dispatch:

permissions:
  issues: read
  pull-requests: read
  contents: read

tools:
  github:
    toolsets: [issues, pull_requests, labels, repos]
    lockdown: false

safe-outputs:
  add-labels:
    allowed: [ext-testlib, fastmodel, gdb, github, good-first-contribution, gpu, gpu-compute, help wanted, learning-gem5,  mem, mem-cache, mem-garnet, mem-ruby, misc, python, question, resources, resources-website, scons, sim, sim-se, stats, stdlib, system-arm, systemc, tests, util, util-docker, util-gem5art, util-m5, website]
    # invalid, low-priority, needs details, Stale, and wontfix excluded from this list
  add-comment: {}
  noop:
    report-as-issue: false
---

# Auto Label Agent - Second Half

Analyze the title and body of the opened PR or issue, then add
zero or more of the allowed labels: `ext-testlib`, `fastmodel`, `gdb`, `github`, `good-first-contribution`, `gpu`, `gpu-compute`, `help wanted`, `learning-gem5`, `mem`, `mem-cache`, `mem-garnet`, `mem-ruby`, `misc`, `python`, `question`, `resources`, `resources-website`, `scons`, `sim`, `sim-se`, `stats`, `stdlib`, `system-arm`, `systemc`, `tests`, `util`, `util-docker`, `util-gem5art`, `util-m5`, `website`.

Do not add the `bug` label to PRs.

Consider the title to be more important than the body when deciding which labels to add.
If something corresponding to a label only comes up 1-2 times in the body,
but isn't mentioned at all in the title, then don't add that label.

Look at the file MAINTAINERS.yaml in the top level of the gem5 repository for information on when some of these labels should be applied.

Aim to have a total of 1-3 labels on each issue/PR, and only apply the most relevant labels.
Keep in mind that this workflow only has some of the labels, and that another workflow will look through the rest of the labels and apply them if they are relevant.

The labels that the other workflow could add are as follows: `arch`, `arch-arm`, `arch-gcn3`, `arch-mips`, `arch-power`, `arch-riscv`, `arch-sparc`, `arch-vega`, `arch-x86`, `base`, `base-stats`, `bug`, `build error`, `classic caches`, `compilation error`, `configs`, `cpu`, `cpu base`, `cpu-kvm`, `cpu-minor`, `cpu-o3`, `cpu-simple`, `dependencies`, `dev`, `dev-arm`, `dev-hsa`, `dev-virtio`, `doc`, `dram`, `duplicate`, `enhancement`, `ext`. If some of these labels are more relevant than the labels that this workflow can apply, then apply fewer labels in this workflow and allow the other workflow to apply the more relevant labels.
