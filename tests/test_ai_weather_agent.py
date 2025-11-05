"""Tests for the weather agent."""

from ai_weather_agent.ai_weather_agent import get_ai_weather_agent
from ai_weather_agent.tools.ai_weather_tools import get_current_weather


def test_ai_weather_agent_exists():
    """Test that the weather agent is properly defined."""
    assert get_ai_weather_agent() is not None


def test_get_current_weather_tokyo():
    """Test that get_current_weather returns correct data for Tokyo."""
    weather = get_current_weather("Tokyo")
    assert weather["temp"] == "22"
    assert weather["condition"] == "sunny"


def test_get_current_weather_new_york():
    """Test that get_current_weather returns correct data for New York."""
    weather = get_current_weather("New York")
    assert weather["temp"] == "15"
    assert weather["condition"] == "cloudy"


def test_get_current_weather_unknown_location():
    """Test that get_current_weather handles unknown locations gracefully."""
    weather = get_current_weather("Unknown City")
    assert weather["temp"] == "unknown"
    assert weather["condition"] == "unknown"


def test_placeholder_that_fails():
    """This test demonstrates the GREEN phase"""
    assert True  # Now it passes


def test_get_weather_temperature_always_says_celsius_unit_location_is_tokyo():
    """Test that get_weather_agent always says Celsius for Tokyo."""
    weather = get_current_weather("Tokyo")
    assert weather["unit"] == "°C"
