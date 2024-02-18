"""CLI entrypoint for simple testing by users.

.. note:: Current implementatoin is stub to pass functests.
"""
from typing import List, Optional

from docutils import nodes
from docutils.core import publish_cmdline
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner


def npm_reference_role(
    role: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Optional[dict] = None,
    content: Optional[List[str]] = None,
):
    """Parse ``npm`` role."""
    options = roles.normalized_role_options(options)
    messages = []
    url = f"https://www.npmjs.com/package/{text}"
    return [nodes.reference(rawtext, text, refuri=url, **options)], messages


def configure():
    """Set up using roles."""
    roles.register_canonical_role("npm", npm_reference_role)
    pass


configure()
publish_cmdline()
