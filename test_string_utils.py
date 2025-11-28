import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


def test_capitalize_basic(utils):
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("Skypro") == "Skypro"
    assert utils.capitalize("s") == "S"
    assert utils.capitalize("123abc") == "123abc"


def test_capitalize_empty_string():
    u = StringUtils()
    assert u.capitalize("") == ""


def test_capitalize_none_raises():
    u = StringUtils()
    with pytest.raises(Exception):
        u.capitalize(None)


def test_trim_leading_spaces():
    u = StringUtils()
    assert u.trim("   skypro") == "skypro"
    assert u.trim(" sky") == "sky"
    # trailing spaces are NOT removed by this implementation
    assert u.trim("  sky  ") == "sky  "


def test_trim_no_leading():
    u = StringUtils()
    assert u.trim("skypro") == "skypro"
    assert u.trim("") == ""


def test_trim_with_tabs_not_removed():
    u = StringUtils()
    assert u.trim("\tsky") == "\tsky"


def test_trim_none_raises():
    u = StringUtils()
    with pytest.raises(Exception):
        u.trim(None)


@pytest.mark.parametrize("text,symbol,expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("abc", "bc", True),
    ("", "", True),
    ("abc", "", True),
    ("", "a", False),
])
def test_contains_various(text, symbol, expected):
    u = StringUtils()
    assert u.contains(text, symbol) == expected


def test_contains_symbol_none_raises_typeerror():
    u = StringUtils()
    with pytest.raises(TypeError):
        u.contains("abc", None)


def test_contains_string_none_raises_typeerror():
    u = StringUtils()
    with pytest.raises(Exception):
        u.contains(None, "a")


def test_delete_symbol_char():
    u = StringUtils()
    assert u.delete_symbol("SkyPro", "k") == "SyPro"
    assert u.delete_symbol("aaa", "a") == ""


def test_delete_symbol_substring():
    u = StringUtils()
    assert u.delete_symbol("SkyPro", "Pro") == "Sky"
    assert u.delete_symbol("aXXaXXa", "XX") == "aaa"


def test_delete_symbol_with_empty_symbol():
    u = StringUtils()
    assert u.delete_symbol("abc", "") == "abc"


def test_delete_symbol_symbol_none_raises():
    u = StringUtils()
    with pytest.raises(TypeError):
        u.delete_symbol("abc", None)


def test_delete_symbol_string_none_raises():
    u = StringUtils()
    with pytest.raises(Exception):
        u.delete_symbol(None, "a")