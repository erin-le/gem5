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

Aim to apply 0-2 new labels, stretching to 3 only if the third label is truly necessary and relevant.
