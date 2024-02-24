import pytest
from rst_package_refs import toolkit


@pytest.mark.parametrize(
    "text,display_text,target_text",
    [
        ("text", "text", "text"),
        ("text <target", "text <target", "text <target"),
        ("text target>", "text target>", "text target>"),
        ("text<target>", "text<target>", "text<target>"),
        ("text <target>", "text", "target"),
        ("text <<target>>", "text", "<target>"),
        ("text <><target>", "text", "><target"),
    ],
)
def test_split_text(text, display_text, target_text):
    display, target = toolkit.split_text(text)
    assert display == display_text
    assert target == target_text


def test_Package_require_inherit():
    with pytest.raises(TypeError):
        package = toolkit.Package.parse("test")
        package.url


def test_InheritPackage():
    class MyPackage(toolkit.Package):
        @property
        def url(self):
            return "ok"

    package = MyPackage.parse("name")
    assert package.url == "ok"
