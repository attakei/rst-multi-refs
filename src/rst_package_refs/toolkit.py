"""Toolkit to create original custom role."""
import re
from typing import Tuple


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
