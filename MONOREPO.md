# AlgoKit Python Monorepo

This repository combines the following AlgoKit Python projects into a single monorepo:

| Directory | Source repository |
| ------------------------------ | ------------------------------------------------------------------------ |
| `algokit-client-generator-py/` | https://github.com/algorandfoundation/algokit-client-generator-py |
| `algokit-subscriber-py/` | https://github.com/algorandfoundation/algokit-subscriber-py |
| `algokit-utils-py/` | https://github.com/algorandfoundation/algokit-utils-py |

It follows the same layout and release process as [algokit-ts](https://github.com/algorandfoundation/algokit-ts).

## Development

Each package is its own [uv](https://docs.astral.sh/uv/) project, with its own `pyproject.toml`, `uv.lock` and `.venv`. Run commands from the package's directory:

```sh
cd algokit-utils-py
uv sync
uv run pytest -n auto   # requires `algokit localnet start`
```

The packages aren't combined into a uv workspace. A workspace has a single `requires-python` for every member, and `algokit-subscriber-py` requires Python 3.12 or later while `algokit-utils-py` and `algokit-client-generator-py` support, and are tested on, 3.10 and 3.11. For the same reason the packages aren't linked to each other's local copies: `algokit-client-generator-py` and `algokit-subscriber-py` still install `algokit-utils` from PyPI, exactly as before the move.

`.pre-commit-config.yaml` is at the root, since pre-commit only reads the config at the repository root. It runs each package's hooks, with that package's files and configuration, in its own uv environment. Ruff runs on the changed files with `uv run --project <package>`, which finds the package's `pyproject.toml` from the file paths. mypy and the docstring check run from the package directory over the files configured in its `pyproject.toml`, as CI does.

## CI

`.github/workflows/ci.yml` runs on pull requests (`pr.yml`) and before every release (`release.yml`). It keeps each package's previous checks and Python versions:

| Job | `algokit-utils-py` | `algokit-client-generator-py` | `algokit-subscriber-py` |
| --- | --- | --- | --- |
| `check`: pip-audit, ruff format and lint, mypy | 3.10, with the docstring check | 3.10, 3.11, 3.12 | 3.12, with the docstring check |
| `test`: pytest against LocalNet, then `uv build` | 3.10, 3.11, 3.12 | 3.10, 3.11, 3.12 | 3.12, 3.13, 3.14, run serially |
| `docs`: build the docs site | yes | (no site) | yes |

The pytest coverage comment is posted once per package, from the lowest Python version, with the package name as its title.

`ci.yml` inherits its permissions from the caller rather than setting them. The coverage comment needs `pull-requests: write`, which `pr.yml` grants, and a reusable workflow can't request a permission its caller doesn't have, so declaring it in `ci.yml` would break `release.yml`.

## Releases

Each package is versioned and released independently with [semfrag](https://github.com/joe-p/semfrag), which replaced python-semantic-release. The packages share the sections in the root `semfrag.json`. Each package has its own `CHANGELOG.md` and `changelog.d/` directory.

Every change to a package's `src/` needs a fragment in that package's `changelog.d/`. The PR workflow checks for one. A fragment is a markdown file with one or more of the sections from `semfrag.json`:

```md
## Fixes

- Describe the change from the user's point of view
```

Fragment sections and the version bump each one triggers:

| Section | Bump |
| ------------------ | ----- |
| `Breaking Changes` | major |
| `Features` | minor |
| `Fixes` | patch |

The release workflow (`.github/workflows/release.yml`) runs after CI passes. It releases the packages one at a time, in dependency order: utils, client-generator, then subscriber. Each package with pending fragments is released like this:

1. **Push to `main`**: the fragments are merged into the changelog and promoted to the next beta, e.g. `4.2.4-beta.5`, which is published to PyPI as a pre-release (`4.2.4b5`).
1. **Manual run with *Stable release?* checked** (*Run workflow*, choosing all packages or one): the package's betas are promoted to a stable release, e.g. `4.2.4`, and published to PyPI. This replaces the old *Production release?* input of the `cd.yaml` workflows.

A manual run with *Stable release?* unchecked (the default) publishes betas exactly like a push to `main`. Use it to retry a push's release that failed and was rolled back: the rollback's revert commit is marked `[skip ci]`, so no push run will release those fragments otherwise.

Each release commits the changelog, the `pyproject.toml` version and `uv.lock` to `main`. The version is written with `uv version`, which uses the normalized PEP 440 form (`4.2.4b5`) and updates the package's own entry in `uv.lock`. Each release also creates a git tag and a GitHub release named after the package, for example `algokit-utils-v4.2.4`, `algokit-client-generator-v2.2.1` and `algokit-subscriber-v1.0.2`, with the built wheel and sdist attached.

Releases start from the exact commit validated by CI. Each package job passes its release commit to the next job; jobs that have nothing to release pass their input commit through unchanged. If unrelated changes advance `main`, the run stops rather than including unvalidated code. A push arriving after the branch check is also protected by the release action's non-force push. Let the newer push's workflow validate and release the remaining changes. For a manual run, dispatch a new run from the latest `main` instead of rerunning the outdated run.

To preview a release locally, run [`semfrag`](https://github.com/joe-p/semfrag#install) from a package directory: `semfrag generate --dry-run`. semfrag finds the root `semfrag.json` by searching the parent directories.

### PyPI trusted publishing

algokit-ts runs each package's release in a reusable workflow (`release-package.yml`). That doesn't work here, because [PyPI trusted publishing can't be used from a reusable workflow](https://github.com/pypa/gh-action-pypi-publish#trusted-publishing): `pypa/gh-action-pypi-publish` has to run in a job of the top-level workflow. Instead:

- The shared steps (checking that `main` hasn't advanced, semfrag's prepare, the version bump, `uv build`, and semfrag's commit, tag and GitHub release) are the local composite action `.github/actions/release-package`.
- Each package's job in `release.yml` calls that action, then `pypa/gh-action-pypi-publish` with `skip-existing: true`, then semfrag's rollback. The rollback is in the same job so a failed upload still rolls back the release; semfrag's actions share their state through the job environment.

## Docs

The `algokit-utils-py` and `algokit-subscriber-py` docs sites are published together to this repository's GitHub Pages site, each under its own path:

| Path | Site |
| -------------- | ------------------------------------------------ |
| `/` | Landing page linking to each site, and to the `algokit-client-generator-py/docs` folder on GitHub (`.github/pages/index.html`) |
| `/utils/` | `algokit-utils-py/docs` |
| `/subscriber/` | `algokit-subscriber-py/docs` |

The docs workflow (`.github/workflows/pages.yml`) runs on every push to `main` and can be run manually. It builds both sites, combines them with the landing page and deploys the result. A repository has only one Pages deployment, so every run rebuilds and replaces all the sites together. Each site is built by the local composite action `.github/actions/build-docs` (previously each repository's `publish-docs` action), which also runs in CI.

Each site reads its URL from environment variables, set by the workflow from `actions/configure-pages` so the sites work under any repository name or custom domain:

- `DOCS_SITE`: the origin, e.g. `https://algorandfoundation.github.io`.
- `DOCS_BASE`: the path the site is served under, e.g. `/algokit-py/utils/`.

Without them the sites fall back to their old standalone paths (`/algokit-utils-py/` and `/algokit-subscriber-py/`), so `uv run poe docs-dev` in a package works as before. To build a site the way it's deployed:

```sh
cd algokit-utils-py
DOCS_BASE=/algokit-py/utils/ uv run poe docs-build
```

The docs sites keep their own `docs/package.json` and `docs/pnpm-lock.yaml`.

### DevPortal

The [Algorand Developer Portal](https://github.com/algorandfoundation/devportal) imports the same docs from a tarball, `devportal-docs.tar.gz`, attached to a rolling GitHub prerelease. The DevPortal docs workflow (`.github/workflows/devportal-docs.yml`) runs on every push to `main` and can be run manually. For each package it builds the docs site, packages its content, sidebar and a `manifest.json`, and uploads the tarball to that package's release:

| Package | Release |
| ----------------------- | -------------------------------- |
| `algokit-utils-py` | `algokit-utils-docs-latest` |
| `algokit-subscriber-py` | `algokit-subscriber-docs-latest` |

The sites are built with their standalone base paths (`/algokit-utils-py/`, `/algokit-subscriber-py/`), which the manifest's `base` passes on so the DevPortal can rewrite links.

## TODO

Outstanding work from the move to a monorepo and semfrag:

- [ ] **PyPI trusted publishing**: each project's trusted publisher on pypi.org still points at its old repository and its `cd.yaml` workflow. Add a trusted publisher for this repository with the workflow `release.yml` and no environment.
- [ ] **Release bot**: `release.yml` uses the `BOT_ID` and `BOT_SK` secrets for the `engineering-ci[bot]` GitHub App, as the old workflows did. Add them to this repository, install the app on it, and allow it to push to `main` if the branch is protected.
- [ ] **Old docs sites**: the `algokit-utils-py` and `algokit-subscriber-py` repositories still serve their last docs build at `algorandfoundation.github.io/algokit-utils-py/` and `/algokit-subscriber-py/`, and it won't be updated. The package READMEs now link to the new site. Turn off Pages in those repositories once the new site is live, or leave the old sites up for existing links.
- [ ] **DevPortal import**: the DevPortal still imports `algokit-utils-py` and `algokit-subscriber-py` docs from the old repositories' `docs-latest` releases. Its import configs need to point at this repository and each package's own release (see [DevPortal](#devportal)), as for algokit-ts.
- [ ] **Subscriber license**: `algokit-subscriber-py` has no `LICENSE` file or `license` field in its `pyproject.toml`, unlike the other two packages.
- [ ] **Links in docstrings**: two docstrings in `algokit-utils-py/src` link to files in the old repository that no longer exist (`docs/source/v3-migration-guide.md`, `docs/source/capabilities/dispenser-client.md`). They were left alone because changing `src/` needs a release fragment.

## How the history was preserved

Each project's full commit history reachable from its `main` branch was imported with a non-squashed subtree merge. Original commits, including their SHAs and signatures, are preserved. The monorepo is the only source of truth for future development; the imports do not require ongoing synchronization with the source repositories.

Files in original commits retain their original root-level paths. The subtree import places them under each project's directory without rewriting those commits. Path-filtered commands such as `git log -- algokit-utils-py/src/...` do not automatically show the pre-import history; inspect an original import SHA with the original paths to explore that history.

The import was done with `git subtree add` (without `--squash`):

```sh
# Start in a new, empty repository
git init -b main
git commit --allow-empty -m "chore: init monorepo"

git subtree add --prefix=algokit-client-generator-py \
  ../../algorandfoundation/algokit-client-generator-py e9aa0fed56bfcf37247b762adfcfbd503b8f7a9d
git subtree add --prefix=algokit-subscriber-py \
  ../../algorandfoundation/algokit-subscriber-py c6b1c59158b7a6b94f6578169b96ce4c698ca18a
git subtree add --prefix=algokit-utils-py \
  ../../algorandfoundation/algokit-utils-py 4bb8bde04aa890c23cdd067bd167c1f0375a632d
```

Notes:

- Only commits reachable from each repo's `main` tip were imported. Unmerged branch history, including the newer development lines (utils `v5.0.0-*`, client-generator `v3.0.0-*`/`v4.0.0-*` and subscriber `v2.0.0-*`), was not imported.
- The source repos were at the following commits when they were imported:
  - `algokit-client-generator-py`: `e9aa0fe` (`2.2.1-beta.3`, 124 commits)
  - `algokit-subscriber-py`: `c6b1c59` (`1.0.2-beta.1`, 169 commits)
  - `algokit-utils-py`: `4bb8bde` (`4.2.4-beta.4`, 306 commits)
- Each source repository's release tags that are ancestors of its imported `main` were imported with the package's tag prefix, pointing to the same original tag objects: `v4.2.3` is `algokit-utils-v4.2.3`, `v2.2.0` is `algokit-client-generator-v2.2.0` and `v1.0.1` is `algokit-subscriber-v1.0.1`. Tags from the unmerged development lines were not imported. For example:

  ```sh
  git fetch --no-tags ../../algorandfoundation/algokit-utils-py \
    refs/tags/v4.2.3:refs/tags/algokit-utils-v4.2.3
  ```

## Changes

Changes made to the imported projects after they were combined into this monorepo.

### semfrag

python-semantic-release was removed: the `[tool.semantic_release]` configuration, the `python-semantic-release` dev dependency, and client-generator's and subscriber's `release-preview` and `release-dry-run-beta` poe tasks. Removing it also removed its dependencies from each `uv.lock`. utils' `gitpython` dev dependency, which only existed to keep python-semantic-release's copy off a vulnerable version, was removed too.

The changelogs were converted from python-semantic-release's format, because semfrag reads every version in the changelog and only accepts the sections in `semfrag.json`:

- Each `## vX.Y.Z (YYYY-MM-DD)` heading became `# X.Y.Z - Month Dth, YYYY`.
- `Fix`/`Bug Fixes`, `Feature`/`Features` and `Breaking` became `Fixes`, `Features` and `Breaking Changes`. Every other section (`Documentation`, `Chores`, `Continuous Integration`, and pull request descriptions that python-semantic-release copied in from merge commits) was dropped, along with each entry's commit-hash link. Issue and pull request links were kept. The original changelogs are in the imported history.
- python-semantic-release only wrote stable releases to the changelog (subscriber's also had its `1.0.0` betas), so each changelog starts with the current beta, which semfrag continues from. Its notes come from the GitHub release: utils' `4.2.4-beta.4` lists the fixes released in its betas since `4.2.3`. Client-generator's `2.2.1-beta.3` and subscriber's `1.0.2-beta.1` only contain chores, so their headings are empty, like algokit-client-generator-ts's first semfrag release.
- Subscriber's `1.0.1` and `1.0.0` were never in its changelog. Empty headings were added for them, dated from their GitHub releases. Its `1.0.0-beta.3` to `beta.6` were published after `1.0.0`, so the blocks are in date order rather than version order.
- Client-generator's `1.0.0` listed "Initial release" three times; it's listed once, under `Breaking Changes`.

utils' `uv.lock` recorded its version as `4.2.4b2`, since python-semantic-release bumped `pyproject.toml` without relocking. It's now `4.2.4b4`, matching `pyproject.toml`. Releases keep them in sync with `uv version`.

### Workflows

Each repository's `.github` directory was removed. The workflows that matter moved to the root as described above:

| Old workflow | Replacement |
| ------------ | ----------- |
| `check-python.yaml`, `build-python.yaml`, `check-docs.yaml` | `ci.yml` |
| `pr.yaml` | `pr.yml`, which also checks for changelog fragments |
| `cd.yaml` (release) | `release.yml` and `.github/actions/release-package` |
| `cd.yaml` (`deploy-docs`) | `pages.yml` |
| `publish-devportal-docs.yml` | `devportal-docs.yml` |
| `.github/actions/publish-docs` | `.github/actions/build-docs`, with a `package` input |

`cd.yaml` skipped CI for commits whose message contained `skip-checks: true`, which python-semantic-release added to its release commits. Release commits are now skipped by actor (`engineering-ci[bot]`) and `[skip ci]`, as in algokit-ts. `cd.yaml` also ignored pushes that only changed `.github/`; `release.yml` runs on every push, but only releases packages with pending fragments.

The issue templates, pull request template and Dependabot config were combined at the root. The issue templates ask which package the issue is about, and Dependabot updates each package's directory.

### Docs

- **Base path**: each `astro.config.mjs` reads `site` and `base` from `DOCS_SITE` and `DOCS_BASE`, falling back to the old values. It uses `||` rather than `??`, since the `build-docs` action passes an empty string when they aren't set.
- **Hardcoded links** (utils): a few hand-written pages link to other pages, and to an image, with absolute paths starting `/algokit-utils-py/`. A remark plugin (`algokit-utils-py/docs/plugins/remark-rebase-links.mjs`) rewrites that prefix to the configured base at build time.
- **Links**: links to files in the old repositories now point at this repository, and links to the old docs sites at the new ones. Two docs pages linked to tests that had moved to `legacy_v2_tests/`, and the utils migration guide linked to a client-generator migration guide under the wrong file name; those links were fixed. The GitHub links in the docs sites' headers point at each package's directory.
