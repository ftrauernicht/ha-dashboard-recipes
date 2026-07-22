## What does this PR change?

<!-- e.g. "Add 2 new dishes", "Fix typo in description of 'lasagne'" -->

## Checklist

- [ ] I only edited `recipes/recipes.json` (or schema/docs, if that's the intent of this PR)
- [ ] Every new/changed entry has a unique, kebab-case `id` that I did not reuse from a removed entry
- [ ] `name` is filled in; `description`, if present, is ≤ 280 characters and factual
- [ ] I ran `python scripts/validate_recipes.py` locally and it passed
