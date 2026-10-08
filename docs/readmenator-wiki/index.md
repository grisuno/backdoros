# Second Brain

*Last synthesized: 2026-10-07 | 3 files | 1 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `backdoros.py`, `fuse_inmem_fs.py`, `getbanners.py`. Architecturally it is 1 layers, dominant utility (3 files) across 1 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Communities are self-contained in the resolved import graph; no cross-boundary bridges were recorded.

Open work clusters around documentation (67% file coverage), 0 security findings, 2 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 3 |
| Symbols | 55 |
| Resolved imports | 0 |
| Languages | py |
| Communities | 1 |
| Doc coverage | 67% (2/3 files) |
| Security findings | 0 |
| Estimated read cost | ~1221 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target readmenator_backdoros_48s0fab6
```

## Concept Wiki

- [root (3 files, cohesion 1.00)](./community_0_root.md)

## God Nodes

| File | Score |
|------|-------|
| `backdoros.py` | 2.9 |
| `fuse_inmem_fs.py` | 2.4 |
| `getbanners.py` | 0.2 |

## Strongest Connections

- No cross-community connections recorded.

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
