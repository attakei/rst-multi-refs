import pytest
from docutils import nodes
from rst_package_refs.registry import pypi


@pytest.fixture
def setup(mocked_roles):
    pypi.setup()
    yield


@pytest.mark.parametrize(
    "source,expected_url",
    [
        (":pypi:`pip`", "https://pypi.org/project/pip"),
        (":pypi:`rst-package-refs`", "https://pypi.org/project/rst-package-refs"),
    ],
)
def test_parse_ok(setup, parse_text, source, expected_url):
    document = parse_text(source)
    refs = list(document.findall(nodes.reference))
    assert len(refs) == 1
    assert refs[0]["refuri"] == expected_url
    assert len(list(document.findall(nodes.problematic))) == 0


@pytest.mark.parametrize("source", [(":pyp:`rst-package-refs`")])
def test_parse_ng(setup, parse_text, source):
    document = parse_text(source)
    refs = list(document.findall(nodes.reference))
    assert len(refs) == 0
    assert len(list(document.findall(nodes.problematic))) > 0
