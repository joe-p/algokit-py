"""Checks the version ranges workspace members declare on each other.

uv ignores a dependency's version range when it uses a workspace source, so the
workspace can resolve, test and release a package against a version of another
member that its published requirements exclude. For example, client-generator
requires `algokit-utils>=4.0.1,<5` but would still be tested against a 5.x
utils from the workspace.

    check            Fail if a member's published requirement on another member
                     excludes that member's current workspace version.
    floor PKG DEP    Print the lowest version of DEP that the package in
                     directory PKG allows, to test against it.

Run with: uv run --no-project --with packaging python .github/scripts/workspace_deps.py check
"""

import sys
import tomllib
from pathlib import Path

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name
from packaging.version import Version

ROOT = Path(__file__).resolve().parents[2]


def load(path: Path) -> dict:
    with path.open("rb") as f:
        return tomllib.load(f)


def members() -> dict[str, tuple[str, dict]]:
    """Map each member's canonical name to its directory and `[project]` table."""
    result = {}
    for directory in load(ROOT / "pyproject.toml")["tool"]["uv"]["workspace"]["members"]:
        project = load(ROOT / directory / "pyproject.toml")["project"]
        result[canonicalize_name(project["name"])] = (directory, project)
    return result


def published_requirements(project: dict) -> list[Requirement]:
    """The requirements that are published with the package (not dev groups)."""
    reqs = list(project.get("dependencies", []))
    for extra in project.get("optional-dependencies", {}).values():
        reqs.extend(extra)
    return [Requirement(r) for r in reqs]


def check() -> int:
    workspace = members()
    errors = []
    for directory, project in workspace.values():
        for req in published_requirements(project):
            dep = workspace.get(canonicalize_name(req.name))
            if dep is None:
                continue
            dep_dir, dep_project = dep
            version = Version(dep_project["version"])
            if not req.specifier.contains(version, prereleases=True):
                errors.append(
                    f"{directory} requires `{req}`, which excludes the workspace's "
                    f"{dep_project['name']} {version} ({dep_dir}). Update the range in "
                    f"{directory}/pyproject.toml so the published package allows the version it's tested with."
                )
            else:
                print(f"ok: {directory} `{req}` allows {dep_project['name']} {version}")
    for error in errors:
        print(f"::error::{error}")
    return 1 if errors else 0


def floor(package_dir: str, dep_name: str) -> int:
    for directory, project in members().values():
        if directory != package_dir:
            continue
        for req in published_requirements(project):
            if canonicalize_name(req.name) != canonicalize_name(dep_name):
                continue
            bounds = [Version(s.version) for s in req.specifier if s.operator in (">=", "==", "~=", "===")]
            if not bounds:
                print(f"`{req}` in {directory} has no lower bound", file=sys.stderr)
                return 1
            print(max(bounds))
            return 0
        print(f"{directory} has no published requirement on {dep_name}", file=sys.stderr)
        return 1
    print(f"{package_dir} is not a workspace member", file=sys.stderr)
    return 1


if __name__ == "__main__":
    match sys.argv[1:]:
        case ["check"]:
            sys.exit(check())
        case ["floor", package_dir, dep_name]:
            sys.exit(floor(package_dir, dep_name))
        case _:
            print(__doc__, file=sys.stderr)
            sys.exit(2)
