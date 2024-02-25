"""NPM registry refecence module."""
from docutils.parsers.rst import roles

from .. import toolkit


class Package(toolkit.Package):
    """Python package published on PyPI."""

    @property
    def url(self):  # noqa: D102
        return f"https://www.npmjs.com/package/{self.name}"


def setup():  # noqa: D103
    roles.register_canonical_role("npm", toolkit.create_simple_reference_role(Package))
