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
  contents: read

tools:
  github:
    toolsets: [issues, pull_requests, labels, repos]
    lockdown: false

safe-outputs:
  add-labels:
    allowed: [arch, arch-arm, arch-gcn3, arch-mips, arch-power, arch-riscv, arch-sparc, arch-vega, arch-x86, base, base-stats, bug, build error, classic caches, compilation error, configs, cpu, cpu base, cpu-kvm, cpu-minor, cpu-o3, cpu-simple, dependencies, dev, dev-arm, dev-hsa, dev-virtio, doc, dram, duplicate, enhancement, ext]
    # wontfix, Stale, and needs details excluded from this list
    # Removed for space:  invalid, low-priority
  add-comment: {}
  noop:
    report-as-issue: false
---

# Auto Label Agent - First Half

Analyze the title and body of the opened PR or issue, then add zero or more of the allowed labels: `arch`, `arch-arm`, `arch-gcn3`, `arch-mips`, `arch-power`, `arch-riscv`, `arch-sparc`, `arch-vega`, `arch-x86`, `base`, `base-stats`, `bug`, `build error`, `classic caches`, `compilation error`, `configs`, `cpu`, `cpu base`, `cpu-kvm`, `cpu-minor`, `cpu-o3`, `cpu-simple`, `dependencies`, `dev`, `dev-arm`, `dev-hsa`, `dev-virtio`, `doc`, `dram`, `duplicate`, `enhancement`, `ext`.

Do not apply the following labels to PRs: `bug`, `build error`, `compilation error`, `duplicate`, `enhancement`

Consider the title to be more important than the body when deciding which labels to add.
If something corresponding to a label only comes up 1-2 times in the body,
but isn't mentioned at all in the title, then don't add that label.

Look at the file MAINTAINERS.yaml in the top level of the gem5 repository for information on when some of these labels should be applied.

Each issue/PR should only have a total of 2-3 labels, and should only have the most relevant labels applied. If a fourth label is truly necessary and relevant, a PR or issue can have up to 4 labels.
This means that generally, this workflow should only apply 1-2 labels, or possibly 3 if none of the relevant labels are applied by the other workflow.
Keep in mind that this workflow only has some of the labels, and that another workflow will look through the rest of the labels and apply them if they are relevant.

The labels that the other workflow could add are as follows: `ext-testlib`, `fastmodel`, `gdb`, `github`, `good-first-contribution`, `gpu`, `gpu-compute`, `help wanted`, `learning-gem5`, `mem`, `mem-cache`, `mem-garnet`, `mem-ruby`, `misc`, `python`, `question`, `resources`, `resources-website`, `scons`, `sim`, `sim-se`, `stats`, `stdlib`, `systemc`, `tests`, `util`, `util-docker`, `util-gem5art`, `util-m5`, `website`. If some of these labels are more relevant than the labels that this workflow can apply, then apply fewer labels in this workflow and allow the other workflow to apply the more relevant labels. Prioritize keeping the number of labels to 3 or less, and do not apply labels for every detail in the issue or PR.

The following list is for PRs only. Only add the specified labels if the PR changes files at the following paths.

- Exception: PR titles typically begin with a list of comma-separated labels, followed by a colon. An example of this is `tests, util:`. If a label is specifically listed in this section of the PR title, then add the label even if the PR doesn't modify the files the label is associated with.

- Only apply labels starting with `arch` if files in `src/arch` are modified.
  - Apply `arch-vega` if files in `src/arch/amdgpu` are modified.
  - If the `arm`, `power`, `riscv`, `sparc`, or `x86` sub-directories in `src/arch` are modified, apply the label that starts with `arch-` and ends with the appropriate directory. For example, if a file in `src/arch/arm` is modified, the label `arch-arm` should be applied.
  - If the files modified in the issue or PR do not fall into any of the directories described above, apply the label `arch`. Do not apply `arch` if any of the labels starting with `arch-` can be applied. For example, if `arch-arm` can be applied, don't apply `arch`.

- Only apply the label `base` if files in `src/base` are modified. If the file is in `src/base/stats`, apply the label `base-stats` instead and don't apply `base`.
- Only apply labels starting with `cpu` if files in `src/cpu` are modified. If the modified files are in the sub-directories `kvm`, `minor`, `o3`, or `simple` in `src/cpu`, the apply the more specific label instead. For example, if a modified file is in `src/cpu/kvm`, then apply the label `cpu-kvm`, and don't apply `cpu`.

- Only apply labels starting with `dev` if files in `src/dev` are modified. If the `arm`, `hsa`, or `virtio` subdirectories in `src/dev` are modified, apply the more specific label and don't apply `dev`. For example, if `src/dev/arm` is modified, apply `dev-arm` and don't apply `dev`.

The following list of restrictions is for reference only, as the following labels are applied by the other workflow.

- Apply `ext-testlib` only if files in `ext/testlib` are modified.

- Apply `fastmodel` only if files in `src/arch/arm/fastmodel` are modified.

- Apply `gpu-compute` only if files in `src/gpu-compute` are modified.

- Apply `learning-gem5` only if files in `src/learning_gem5` are modified
- Apply labels starting with `mem` only if files in `src/mem` are modified.
  - If `src/mem/cache` modified: apply `mem-cache`
  - If `src/mem/ruby`: apply `mem-ruby`
  - If `src/mem/ruby/network/garnet`: apply `mem-garnet`
  - If the files modified aren't in any of the above directories, then apply `mem`. Don't apply `mem` if any of `mem-cache`, `mem-ruby`, or `mem-garnet` can be applied.

- Apply `python` only if files in `src/python` are modified. If the only files modified are in `src/python/gem5`, apply `stdlib` instead, and don't apply `python`.
- Apply `sim` only if files in `src/sim` are modified.
- For PRs, only apply `systemc` if files in `src/systemc` are modified
- For PRs, only apply `tests` if files in `tests/` are modified
- Only apply labels starting with `util` if files in `util/` are modified. If files in the subdirectories `dockerfiles`, `gem5art`, or `m5` are modified, apply the corresponding label starting with `util`, and don't apply `util`. For example, if a file in `util/m5` is modified, apply the label `util-m5` and don't apply `util`. For files in `util/dockerfiles`, the label `util-docker` should be applied.

The following information applies to both workflows. The labels `arch`, `base`, `cpu`, `ext`, `mem`, `python`, and `util`, are all "generic" labels that have "more specific" labels. "More specific" labels are labels that start with one of the generic labels, followed by a dash (-) and another word. For example, `arch-arm` would be one of the more specific labels for `arch`. For both PRs and issues, apply the more specific label if possible (i.e. if it is relevant and is one of the labels this workflow is allowed to add), and don't apply the generic label if a more specific label is applied. For example, if the label `arch-arm` can be applied, then apply that label, and don't apply `arch`.

- as mentioned above, the more specific label for `python` is `stdlib`, which should be applied to files in `src/python/gem5`.
