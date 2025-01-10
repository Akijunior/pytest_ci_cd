"""Pytest course."""

from main import soma


def test_soma():
    """Test Soma."""
    assert soma(2, 3) == 5
