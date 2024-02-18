"""Sphinx extension handler module."""
from sphinx.application import Sphinx
from sphinx.config import Config

from .core import configure


def register_roles(app: Sphinx, config: Config):
    """Add custom role based from Sphix configrations."""
    configure()


def setup(app: Sphinx):
    """Entrypoint as Sphinx extension."""
    app.connect("config-inited", register_roles)
    return {
        "version": "0.0.0",
        "env_version": 1,
        "parallel_read_safe": False,
    }
