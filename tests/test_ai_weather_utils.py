"""Tests for utility functions."""

from ai_weather_agent.ai_weather_utils import format_weather_report


def test_format_weather_report_tokyo():
    """Test that format_weather_report returns correctly formatted report for Tokyo."""
    report = format_weather_report("Tokyo")
    assert "Tokyo" in report
    assert "22°C" in report
    assert "sunny" in report


def test_format_weather_report_new_york():
    """Test that format_weather_report returns correctly formatted report for New York."""
    report = format_weather_report("New York")
    assert "New York" in report
    assert "15°C" in report
    assert "cloudy" in report


def test_format_weather_report_unknown_location():
    """Test that format_weather_report handles unknown locations gracefully."""
    report = format_weather_report("Unknown City")
    assert "not available" in report.lower()
    assert "Unknown City" in report
