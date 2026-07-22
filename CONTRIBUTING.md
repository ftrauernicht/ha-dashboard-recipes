# Contributing

Thanks for wanting to add or change a dish!

## Ground rules

- All changes land via Pull Request. Direct pushes to `main` are blocked for everyone, including the maintainer — this is enforced by branch protection, not just a convention.
- Keep PRs focused: one logical change (e.g. "add 3 dishes", "fix typo in X") per PR.
- The automated `Validate recipes.json` check must pass before a PR can be merged.

## How to add or change a dish

1. Fork the repo and create a branch.
2. Edit [`recipes/recipes.json`](recipes/recipes.json). Add or change an entry:
   ```json
   { "id": "your-dish-id", "name": "Your Dish Name", "description": "Optional short description." }
   ```
3. Validate locally before opening the PR:
   ```bash
   pip install jsonschema
   python scripts/validate_recipes.py
   ```
4. Open a Pull Request against `main`. The PR template has a checklist — fill it in.

## `id` guidelines

- Lowercase, ASCII, kebab-case (`^[a-z0-9]+(-[a-z0-9]+)*$`), e.g. `spaghetti-bolognese`.
- Must be unique across the whole file.
- Never reuse an `id` that was removed, and never change an existing `id` — it's a stable key that other systems (the Home Assistant dashboard) may already refer to.

## `description` guidelines

- Optional. Not shown on the dashboard today, but reserved for a future detail view — write it as if it will be shown.
- Max 280 characters, factual, no links or promotional text.
