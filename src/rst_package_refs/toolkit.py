"""Toolkit to create original custom role."""
import abc
import re
from dataclasses import dataclass
from typing import Tuple


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
