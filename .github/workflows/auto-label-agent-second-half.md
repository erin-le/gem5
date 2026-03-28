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
    allowed: [ext-testlib, fastmodel, gdb, github, good-first-contribution, gpu, gpu-compute, help wanted, learning-gem5,  mem, mem-cache, mem-garnet, mem-ruby, misc, python, question, resources, resources-website, scons, sim, sim-se, stats, stdlib, system-arm, systemc, tests, util, util-docker, util-m5, website]
    # wontfix, Stale, and needs details excluded from this list
    # Removed for space:  invalid, low-priority, util-gem5art,
  add-comment: {}
  noop:
    report-as-issue: false
---

# Auto Label Agent - Second Half

Analyze the title and body of the opened PR or issue, then add
zero or more of the allowed labels: `ext-testlib`, `fastmodel`, `gdb`, `github`, `good-first-contribution`, `gpu`, `gpu-compute`, `help wanted`, `learning-gem5`, `low-priority`, `mem`, `mem-cache`, `mem-garnet`, `mem-ruby`, `misc`, `python`, `question`, `resources`, `resources-website`, `scons`, `sim`, `sim-se`, `stats`, `stdlib`, `system-arm`, `systemc`, `tests`, `util`, `util-docker`, `util-m5`, `website`.

Consider the title to be more important than the body when deciding which labels to add.
If something corresponding to a label only comes up 1-2 times in the body,
but isn't mentioned at all in the title, then don't add that label.

Look at the file MAINTAINERS.yaml in the top level of the gem5 repository for information on when some of these labels should be applied.

Aim to apply 0-2 new labels, stretching to 3 only if the third label is truly necessary and relevant.
