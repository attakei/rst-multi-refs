#!/usr/bin/env python
"""Batch script to generate 'release' commit."""
import argparse
import subprocess
from pathlib import Path

import tomllib

root = Path(__file__).parent.parent
parser = argparse.ArgumentParser()
parser.add_argument("level", type=str, choices=["major", "minor", "patch"])


def get_version() -> str:  # noqa: D103
    cmd = ["rye", "version"]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE)
    return proc.stdout.decode("utf-8").strip()


def bump_version(level: str) -> str:  # noqa: D103
    """Bump version for sources."""
    cmd = ["rye", "version", "--bump", level]
    subprocess.run(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return get_version()


def replace_version(target, current_version: str, new_version: str):
    """Change old/new version text from source."""
    src = root / target["filename"]
    lines = []
    from_ = target["search"].format(current_version=current_version)
    to_ = target["replace"].format(new_version=new_version)
    for line in src.read_text().split("\n"):
        if line == from_:
            lines.append(to_)
        else:
            lines.append(line)
    src.write_text("\n".join(lines))


def main(args: argparse.Namespace):
    """Handle multi functions."""
    pyproject = tomllib.loads((root / "pyproject.toml").read_text())
    current_version = get_version()
    print(f"Current version: v{current_version}")
    new_version = bump_version(args.level)
    print(f"Next version:    v{new_version}")
    for target in pyproject["tool"]["local"]["bumpversion"]["files"]:
        replace_version(target, current_version, new_version)
    pass


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
