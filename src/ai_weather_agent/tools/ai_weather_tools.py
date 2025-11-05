"""Weather tool for the AI agent."""


def get_current_weather(location: str) -> dict:
    """
    Get the current weather for a location.

    This is a placeholder implementation. In production, this would call a real weather API.

    Args:
        location: The location to get weather for (e.g., "Tokyo", "New York")

    Returns:
        A dictionary with 'temp' and 'condition' keys
    """
    # Placeholder data - in production, call a real weather API
    weather_data = {
        "Tokyo": {"temp": "22", "condition": "sunny", "unit": "°C"},
        "New York": {"temp": "15", "condition": "cloudy", "unit": "°C"},
        "London": {"temp": "12", "condition": "rainy", "unit": "°C"},
        "Sydney": {"temp": "25", "condition": "sunny", "unit": "°C"},
    }
    return weather_data.get(location, {"temp": "unknown", "condition": "unknown"})
