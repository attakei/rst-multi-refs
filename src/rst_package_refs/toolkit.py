"""Toolkit to create original custom role."""
import abc
import re
from dataclasses import dataclass
from typing import List, Optional, Tuple, Type

from docutils import nodes
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner


@dataclass
class Package(abc.ABC):
    """Package data struct (abstract)."""

    name: str

    @property
    @abc.abstractmethod
    def url(self) -> str:
        """Return URL of package."""
        pass

    @classmethod
    def parse(cls, target) -> "Package":
        """Parse target and generate package object.

        If your definition package requires extra method to parse, override it.
        """
        return cls(name=target)


def create_reference_role(package_class: Type[Package]) -> callable:
    """Create custom-role function for assigned package type."""

    def _reference_role(
        role: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Inliner,
        options: Optional[dict] = None,
        content: Optional[List[str]] = None,
    ):
        options = roles.normalized_role_options(options)
        messages = []
        package = package_class.parse(text)
        return [nodes.reference(rawtext, text, refuri=package.url, **options)], messages

    return _reference_role


def split_text(source: str) -> Tuple[str, str]:
    """Split from content to displaying text and target text.

    Support text patterns:

    * ``text <target>``
    * ``target``
    """
    matched = re.match(r"^(?P<display>.+) <(?P<target>.+)>$", source)
    if matched:
        return matched.group("display"), matched.group("target")
    return source, source
