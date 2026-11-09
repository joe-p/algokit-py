# AlgoKit Python

This monorepo contains the core Python libraries and tools for [AlgoKit](https://github.com/algorandfoundation/algokit-cli), making it easier to build, test, deploy, and index applications on the Algorand blockchain.

## Packages

| Package | Directory | Description | Docs |
| ------- | --------- | ----------- | ---- |
| [`algokit-utils`](https://pypi.org/project/algokit-utils/) | [`algokit-utils-py/`](./algokit-utils-py) | Core Algorand utilities providing a high-level, intuitive interface over `py-algorand-sdk`. | [Docs](https://algorandfoundation.github.io/algokit-py/utils/) · [README](./algokit-utils-py/README.md) |
| [`algokit-client-generator`](https://pypi.org/project/algokit-client-generator/) | [`algokit-client-generator-py/`](./algokit-client-generator-py) | Generates type-safe Python clients for ARC-56 and ARC-32 smart contracts. | [Usage](./algokit-client-generator-py/docs/usage.md) · [README](./algokit-client-generator-py/README.md) |
| [`algokit-subscriber`](https://pypi.org/project/algokit-subscriber/) | [`algokit-subscriber-py/`](./algokit-subscriber-py) | Configurable transaction subscription and indexing library for Algorand. | [Docs](https://algorandfoundation.github.io/algokit-py/subscriber/) · [README](./algokit-subscriber-py/README.md) |

## Requirements

- **[uv](https://docs.astral.sh/uv/)**: each package is a uv project with its own `uv.lock`
- **Python**: `>=3.10` for `algokit-utils-py` and `algokit-client-generator-py`, `>=3.12` for `algokit-subscriber-py`
- **[AlgoKit CLI](https://github.com/algorandfoundation/algokit-cli)**: required to run LocalNet for integration tests (`algokit localnet start`)
- **Node.js and pnpm**: only to build the docs sites

## Development

Each package is developed from its own directory:

```sh
cd algokit-utils-py

uv sync                # create .venv with the package and its dev dependencies
uv run pytest -n auto  # run the tests (requires `algokit localnet start`)

# Format, lint, type-check and audit
uv run ruff format .
uv run ruff check .
uv run mypy
uv run pip-audit
```

`algokit-subscriber-py`'s tests aren't parallel-safe, so run them without `-n auto`.

Pre-commit hooks for all three packages are configured in the root [`.pre-commit-config.yaml`](./.pre-commit-config.yaml). Install them from the repository root with:

```sh
uv run --project algokit-utils-py pre-commit install
```

### Documentation

The documentation sites for `algokit-utils-py` and `algokit-subscriber-py` are built with Sphinx (API reference) and Astro Starlight, and deployed together to [GitHub Pages](https://algorandfoundation.github.io/algokit-py/):

```sh
cd algokit-utils-py
pnpm install --dir docs
uv run poe docs-dev     # generate the API reference and start a dev server
uv run poe docs-build   # generate the API reference and build the site
```

## Contributing & Releases

Each package is versioned and released independently using [semfrag](https://github.com/joe-p/semfrag).

Any pull request that modifies a package's `src/` directory must include a changelog fragment file in that package's `changelog.d/` directory (e.g., `algokit-utils-py/changelog.d/my-change.md`) containing one or more of the sections defined in [`semfrag.json`](./semfrag.json):

```markdown
## Fixes

- Describe the change from the user's point of view
```

| Section            | Version Bump |
| ------------------ | ------------ |
| `Breaking Changes` | `major`      |
| `Features`         | `minor`      |
| `Fixes`            | `patch`      |

- **Beta releases**: Pushing to `main` automatically merges pending fragments into each package's `CHANGELOG.md` and publishes a beta version to PyPI.
- **Stable releases**: Running the [Release workflow](./.github/workflows/release.yml) manually with *Stable release?* checked promotes pending beta versions to a stable release on PyPI.
- **Retrying a beta release**: Running the workflow manually with *Stable release?* unchecked (the default) publishes betas like a push does, to retry a push's release that failed and was rolled back.

For details on CI, releases, docs publishing, and how the repository history was combined, see [`MONOREPO.md`](./MONOREPO.md).

## License

`algokit-utils-py` and `algokit-client-generator-py` are licensed under the [MIT License](./algokit-utils-py/LICENSE).
