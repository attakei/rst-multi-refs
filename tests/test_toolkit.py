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
