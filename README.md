# The Houseplant Out-of-Office

[![make.fun bounty](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/aint965/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/aint965/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

An entry for the [make.fun bounty "The Houseplant Out-of-Office"](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047): the funniest out-of-office auto-reply a houseplant would send, in 120 characters or fewer. This houseplant is away from its desk — which is a windowsill — hasn't had a drink since March, and, in the grand tradition of out-of-office replies, helpfully redirects all correspondence to the only colleague still on duty: the cactus.

> I'm away from my desk (a windowsill). My last drink was in March. Please direct all emails to the cactus.

## How to run

```sh
python3 main.py
```

This writes the auto-reply to `entry.txt` in the output directory (`/output` by default, or wherever `MAKEFUN_OUTPUT_DIR` points). The program is deterministic, dependency-free, and refuses to write a line longer than 120 characters.
