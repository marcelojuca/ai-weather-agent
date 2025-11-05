"""Utility functions for the weather agent."""

from ai_weather_agent.tools.ai_weather_tools import get_current_weather


def do_something_useful():
    """Display current weather information."""
    print("Replace this with a utility function")


def format_weather_report(location: str) -> str:
    """
    Format weather information for a location into a readable report.

    Args:
        location: The location to get weather for

    Returns:
        A formatted weather report string
    """
    weather = get_current_weather(location)
    temp = weather.get("temp", "unknown")
    condition = weather.get("condition", "unknown")
    unit = weather.get("unit", "")

    if temp == "unknown":
        return f"Weather data for '{location}' is not available."

    return f"🌤️  {location}: {temp}{unit} and {condition}"
