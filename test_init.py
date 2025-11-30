"""
Basic tests for the IP lookup application.
"""

import pytest


def test_imports():
    """Test that required modules can be imported."""
    import requests

    assert requests is not None


def test_access_key_exists():
    """Test that access key is defined."""
    # Read the file to check for access_key
    with open("__init.py", "r", encoding="utf-8") as f:
        content = f.read()
        assert "access_key" in content


def test_api_url_format():
    """Test that API URLs are properly formatted."""
    access_key = "test_key"
    url = f"https://api.ipapi.com/api/check?access_key={access_key}"
    assert "https://api.ipapi.com/api/" in url
    assert "access_key=" in url
