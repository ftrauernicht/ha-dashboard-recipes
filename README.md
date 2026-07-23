# ha-dashboard-recipes

A community-editable list of dishes ("Gerichte") used by a Home Assistant dashboard tile that picks a random dish for dinner. The data lives here, in this public repo, instead of hardcoded in a Home Assistant YAML file — so it can be extended via Pull Request without touching the Home Assistant config directly.

## Data format

The single source of truth is [`recipes/recipes.json`](recipes/recipes.json), validated against [`schema/recipes.schema.json`](schema/recipes.schema.json) (JSON Schema, draft 2020-12).

```json
{
  "recipes": [
    {
      "id": "spaghetti-bolognese",
      "name": "Spaghetti Bolognese",
      "description": "Klassische Sauce mit Rinderhack, Tomaten und Parmesan."
    },
    {
      "id": "salat",
      "name": "Salat"
    }
  ]
}
```

Fields:

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Stable, unique, kebab-case slug. Never changed or reused once published — it's a stable key, other systems may refer to it. |
| `name` | yes | Display name, shown on the dashboard tile. |
| `description` | no | Longer free text. **Not currently rendered** by the dashboard tile, but reserved for a future detail view (e.g. a popup on tap). Keep it short (≤ 280 chars) and factual. |

## Contributing

All changes to `recipes/recipes.json` happen through Pull Requests — direct pushes to `main` are blocked by branch protection, for everyone including the maintainer. See [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and validation steps.

## Using this repo from Home Assistant

The repo is public, so the raw data file can be polled directly, no authentication needed:

```
https://raw.githubusercontent.com/ftrauernicht/ha-dashboard-recipes/main/recipes/recipes.json
```

For the full picture — a sensor that avoids repeating recent picks, the picking script, and a ready-to-paste dashboard card (with a screenshot) — see **[docs/home-assistant-setup.md](docs/home-assistant-setup.md)**.

Minimal example if you just want the raw list as a sensor attribute:

```yaml
rest:
  - resource: https://raw.githubusercontent.com/ftrauernicht/ha-dashboard-recipes/main/recipes/recipes.json
    scan_interval: 3600 # raw.githubusercontent.com is CDN-cached for a few minutes; polling more often than that has no effect
    sensor:
      - name: "Dish List"
        unique_id: dish_list
        value_template: "loaded"
        json_attributes:
          - recipes
```

The `recipes` attribute is a list of `{id, name, description}` objects. A consuming script/template can pull out `name`, e.g.:

```jinja
{{ state_attr('sensor.dish_list', 'recipes') | map(attribute='name') | list }}
```

To force an immediate refresh instead of waiting for `scan_interval`, call `homeassistant.update_entity` on `sensor.dish_list`.

## License

[MIT](LICENSE).
