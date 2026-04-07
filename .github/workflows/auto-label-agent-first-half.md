---
timeout-minutes: 5

on:
  issues:
    types: [opened]
  pull_request:
    types: [opened]

# on:
#   schedule: daily
#   workflow_dispatch:

permissions:
  issues: read
  pull-requests: read

tools:
  lockdown: false
  github:
    toolsets: [issues, pull_requests, labels]

safe-outputs:
  add-labels:
    allowed: [arch, arch-arm, arch-gcn3, arch-mips, arch-power, arch-riscv, arch-sparc, arch-vega, arch-x86, base, base-stats, bug, build error, classic caches, compilation error, configs, cpu, cpu base, cpu-kvm, cpu-minor, cpu-o3, cpu-simple, dependencies, dev, dev-arm, dev-hsa, dev-virtio, doc, dram, duplicate, enhancement, ext]
    # wontfix, Stale, and needs details excluded from this list
    # Removed for space:  invalid, low-priority, util-gem5art,
  add-comment: {}
  noop:
    report-as-issue: false
---

# Auto Label Agent - First Half

Analyze the title and body of the opened PR or issue, then add zero or more of the allowed labels: `arch`, `arch-arm`, `arch-gcn3`, `arch-mips`, `arch-power`, `arch-riscv`, `arch-sparc`, `arch-vega`, `arch-x86`, `base`, `base-stats`, `bug`, `build error`, `classic caches`, `compilation error`, `configs`, `cpu`, `cpu base`, `cpu-kvm`, `cpu-minor`, `cpu-o3`, `cpu-simple`, `dependencies`, `dev`, `dev-arm`, `dev-hsa`, `dev-virtio`, `doc`, `dram`, `duplicate`, `enhancement`, `ext`.

Do not add the `bug` label to PRs.

Consider the title to be more important than the body when deciding which labels to add.
If something corresponding to a label only comes up 1-2 times in the body,
but isn't mentioned at all in the title, then don't add that label.

Look at the file MAINTAINERS.yaml in the top level of the gem5 repository for information on when some of these labels should be applied.

Aim to have a total of 1-3 labels on each issue/PR, and only apply the most relevant labels.
Keep in mind that this workflow only has some of the labels, and that another workflow will look through the rest of the labels and apply them if they are relevant.

The labels that the other workflow could add are as follows: `ext-testlib`, `fastmodel`, `gdb`, `github`, `good-first-contribution`, `gpu`, `gpu-compute`, `help wanted`, `learning-gem5`, `low-priority`, `mem`, `mem-cache`, `mem-garnet`, `mem-ruby`, `misc`, `python`, `question`, `resources`, `resources-website`, `scons`, `sim`, `sim-se`, `stats`, `stdlib`, `system-arm`, `systemc`, `tests`, `util`, `util-docker`, `util-m5`, `website`. If some of these labels are more relevant than the labels that this workflow can apply, then apply fewer labels in this workflow and allow the second workflow to apply the more relevant labels.
