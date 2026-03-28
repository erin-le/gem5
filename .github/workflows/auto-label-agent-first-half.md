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
---

# Auto Label Agent

Analyze the title and body of the opened PR or issue, then add zero or more of the allowed labels: `arch`, `arch-arm`, `arch-gcn3`, `arch-mips`, `arch-power`, `arch-riscv`, `arch-sparc`, `arch-vega`, `arch-x86`, `base`, `base-stats`, `bug`, `build error`, `classic caches`, `compilation error`, `configs`, `cpu`, `cpu base`, `cpu-kvm`, `cpu-minor`, `cpu-o3`, `cpu-simple`, `dependencies`, `dev`, `dev-arm`, `dev-hsa`, `dev-virtio`, `doc`, `dram`, `duplicate`, `enhancement`, `ext`.

Do not add the `bug` label to PRs.
