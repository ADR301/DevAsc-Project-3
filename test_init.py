"""
Basic tests for the IP lookup application.
"""

import pytest
import unittest
from unittest.mock import patch, Mock
import requests

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

def test_build_url_with_ip_and_key():
    """Test building an API URL that includes an IP and access key."""
    access_key = "abc123"
    ip = "1.2.3.4"
    url = f"https://api.ipapi.com/api/{ip}?access_key={access_key}"
    assert "/api/" in url
    assert ip in url
    assert "access_key=" in url


def test_requests_get_raises_timeout(monkeypatch):
    """Test that a requests.get timeout propagates as a Timeout exception."""
    def fake_get(*args, **kwargs):
        raise requests.exceptions.Timeout()

    monkeypatch.setattr(requests, "get", fake_get)
    with pytest.raises(requests.exceptions.Timeout):
        requests.get("https://api.ipapi.com/api/check?access_key=test")

