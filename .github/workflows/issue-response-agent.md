---
timeout-minutes: 5

on:
  issues:
    types: [opened]

permissions:
  issues: read

tools:
  lockdown: false
  github:
    toolsets: [issues]

safe-outputs:
  add-comment: {}
  noop:
    report-as-issue: false

---

# Issue Auto-Response Agent

If an issue is about an unimplemented system call, or syscall, in gem5, then
ping the author and respond with a polite, encouraging, and concise message about how
unimplemented system calls in SE mode aren't considered to be bugs, but rather
unimplemented features. Further state that the author is welcome to open a PR
to add the missing syscalls if they want.

A sample message is as follows, where `author-name` should be replaced with the
GitHub username of the issue's author:

```txt
@author-name: Hello, thanks for opening this issue. Unimplemented syscalls aren't really
considered bugs in gem5, but rather unimplemented features. If you continue
working on this, please feel free to open a PR to add these syscalls. Thank you!
```
