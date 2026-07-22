#!/usr/bin/env python3
"""Validate recipes/recipes.json against schema/recipes.schema.json plus id-uniqueness."""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "recipes" / "recipes.json"
SCHEMA_PATH = ROOT / "schema" / "recipes.schema.json"


def main():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if errors:
        for error in errors:
            print(f"schema error at {list(error.path)}: {error.message}", file=sys.stderr)
        sys.exit(1)

    ids = [recipe["id"] for recipe in data["recipes"]]
    duplicates = sorted({i for i in ids if ids.count(i) > 1})
    if duplicates:
        print(f"duplicate recipe ids: {duplicates}", file=sys.stderr)
        sys.exit(1)

    print(f"OK: {len(ids)} recipes validated")


if __name__ == "__main__":
    main()
