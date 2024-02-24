import copy

import pytest
from docutils import nodes
from docutils.frontend import get_default_settings
from docutils.parsers.rst import Parser, roles
from docutils.utils import new_document


@pytest.fixture
def mocked_roles(monkeypatch):
    _role_registry = copy.deepcopy(roles._role_registry)
    monkeypatch.setattr(roles, "_role_registry", _role_registry)
    yield


@pytest.fixture
def parse_text():
    def _parse_text(source) -> nodes.document:
        parser = Parser()
        settings = get_default_settings(Parser)
        settings.warning_stream = ""
        document = new_document("test data", settings.copy())
        parser.parse(source, document)
        return document

    return _parse_text
