# backend/tests/test_validation.py
import pytest
from tts_utils import validate_text

def test_validate_text_basic():
    assert validate_text(" hello ") == "hello"
    with pytest.raises(ValueError):
        validate_text("")  # empty string
    with pytest.raises(ValueError):
        validate_text(None)  # not a string

def test_validate_text_length():
    s = "a" * 6000
    with pytest.raises(ValueError):
        validate_text(s, max_len=5000)

def test_control_characters_removed():
    t = "Line1\x03Line2"
    out = validate_text(t)
    assert "\x03" not in out
