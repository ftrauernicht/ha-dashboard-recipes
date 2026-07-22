# CLAUDE.md

Guidance for Claude Code (or any AI coding agent) working in this repository.

## What this repo is

This repo's only job is to be a single source of truth for `recipes/recipes.json`, which is polled live over HTTPS (`raw.githubusercontent.com`) by a Home Assistant dashboard tile that picks a random dish. There is no build step and no application code here — treat `recipes/recipes.json` as a small public data API, not as internal project config.

## Hard rules

- **Never commit directly to `main`.** Always work on a branch and open a Pull Request. Branch protection enforces this for everyone including the repo owner — do not attempt to bypass it (e.g. force-push, disabling the ruleset) even if you technically have the access to do so.
- The only data file is `recipes/recipes.json`; it must always validate against `schema/recipes.schema.json`. Run `python scripts/validate_recipes.py` after any edit — the same check gates merging in CI.
- `id` is a stable external key. Never change or remove an existing `id`. If a dish is retired, either leave its entry as-is or remove it entirely — but never recycle its `id` for a different dish.
- `name` is required and rendered directly on the dashboard. `description` is optional and currently unused by the UI, but is reserved for a future detail view — keep it short (≤ 280 chars) and factual, not a placeholder.
- Don't add new top-level fields to a recipe without updating `schema/recipes.schema.json`, `scripts/validate_recipes.py` (if it needs new checks), `README.md`, and this file together in the same PR — downstream (Home Assistant) has no visibility into this repo's history and can only go on what's documented here.

## Repo layout

- `recipes/recipes.json` — the data.
- `schema/recipes.schema.json` — JSON Schema (draft 2020-12) that `recipes.json` must satisfy.
- `scripts/validate_recipes.py` — schema validation + duplicate-`id` check; run locally and in CI.
- `.github/workflows/validate.yml` — CI job (`Validate recipes.json`) required by branch protection before merge.
