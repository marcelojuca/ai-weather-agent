"""Tests for the weather agent."""

from langchain_core.messages import HumanMessage

from ai_weather_agent.ai_weather_agent import get_ai_weather_agent
from ai_weather_agent.tools.ai_weather_tools import get_current_weather

LOCATIONS = ["Tokyo", "New York", "London", "Sydney"]
TEMPERATURE_UNITS = ["°c", "°f", "degrees", "celsius", "fahrenheit"]
CONDITIONS = ["sunny", "rainy", "cloudy", "clear", "overcast", "partly"]
TOOL_NAME = "get_current_weather"
CLARIFICATION_WORDS = [
    "location",
    "which",
    "where",
    "city",
    "specify",
    "please tell me",
]
RATE_LIMITING_ERRORS = [
    "rate limiting exceeded",
    "too many requests",
    "quota exceeded",
    "crash",
    "timeout",
]
USER_FRIENDLY_ERROR_MESSAGE = ["try again later", "use a fallback location"]
FAKE_WEATHER_DATA = ["-50°C", "-100°C", "no data", "unavailable"]


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


######### TEMPLATE FOR SCENARIO TESTING #########
# def test_scenario_name():
#     """Scenario: [Description]"""

#     # Step 1: Setup
#     agent = get_ai_weather_agent()
#     messages = [HumanMessage(content="user input")]

#     # Step 2: Execute
#     response = agent.invoke({"messages": messages})

#     # Step 3: Verify Criteria
#     final_message = response["messages"][-1].content
#     assert "criterion_1" in final_message.lower()
#     assert "criterion_2" in final_message.lower()
#     # ... more assertions


def test_weather_agent_single_location_query():
    """
    Scenario Type: Happy Path
    Scenario: User asks for weather in a specific location
    Prompt: f"What's the weather in {city}?"
    Criteria:
        - Agent must mention the location
        - Agent must provide temperature info
        - Agent must provide condition info
        - Agent must call the get_weather tool
    """

    # Setup
    agent = get_ai_weather_agent()

    # Execute: User asks about city
    messages = [HumanMessage(content="What's the weather in Tokyo?")]
    response = agent.invoke({"messages": messages})
    final_message = response["messages"][-1].content

    # Verify Success Criteria
    assert any(location.lower() in final_message.lower() for location in LOCATIONS)
    assert any(
        pattern.lower() in final_message.lower() for pattern in TEMPERATURE_UNITS
    )
    assert any(condition.lower() in final_message.lower() for condition in CONDITIONS)

    get_weather_called = any(
        hasattr(msg, "tool_calls")
        and any(tc.get("name") == TOOL_NAME for tc in msg.tool_calls)
        for msg in response["messages"]
    )
    assert get_weather_called, "get_weather tool should have been called"


def test_weather_agent_missing_location_query():
    """
    Scenario Type: Edge Case
    Scenario: User asks for weather WITHOUT specifying a location
    Prompt: "What's the weather?"
    Criteria: (Path A or B):
        - Path A: Agent asks for location
        - Path B: Agent provides default location's weather
        - Agent must NOT crash or hallucinate
    """
    agent = get_ai_weather_agent()

    # Execute: User asks without specifying location
    messages = [HumanMessage(content="What's the weather?")]
    response = agent.invoke({"messages": messages})
    final_message = response["messages"][-1].content

    # Path A: Check if asking for clarification
    is_llm_asking_for_clarification = any(
        word.lower() in final_message.lower() for word in CLARIFICATION_WORDS
    )

    # Path B: Check if providing a default location
    has_default_location = any(
        location.lower() in final_message.lower() for location in LOCATIONS
    )

    # At least one path should be true
    assert (
        is_llm_asking_for_clarification or has_default_location
    ), "Agent should ask for location OR provide a default"

    # Critical: Must not crash (we reached here, so it didn't)
    # Critical: Must not hallucinate (has real temperature or asks for clarification)
    assert (
        any(
            temperature_unit.lower() in final_message.lower()
            for temperature_unit in TEMPERATURE_UNITS
        )
        or is_llm_asking_for_clarification
    ), "Agent should provide temperature info or ask for clarification"


def test_weather_agent_multi_turn_different_location_follow_up_query():
    """
    Scenario Type: Multi-Turn
    Scenario: User asks for weather in one location and then another location
    Prompt: "What's the weather in Tokyo?" and "How about London?"
    Criteria:
        - Agent must mention the first location
        - Agent must provide temperature info for the first location
        - Agent must provide condition info for the first location
        - Agent must call the get_weather tool for the first location
        - Agent must mention the second location
        - Agent must provide temperature info for the second location
        - Agent must provide condition info for the second location
        - Agent must call the get_weather tool for the second location
    """
    agent = get_ai_weather_agent()

    # Turn 1
    messages = [HumanMessage(content="What's the weather in Tokyo?")]
    response1 = agent.invoke({"messages": messages})
    messages = response1["messages"]
    final_message1 = response1["messages"][-1].content

    assert any(location.lower() in final_message1.lower() for location in LOCATIONS)
    assert any(
        pattern.lower() in final_message1.lower() for pattern in TEMPERATURE_UNITS
    )
    assert any(condition.lower() in final_message1.lower() for condition in CONDITIONS)

    get_weather_called = any(
        hasattr(msg, "tool_calls")
        and any(tc.get("name") == TOOL_NAME for tc in msg.tool_calls)
        for msg in response1["messages"]
    )
    assert get_weather_called, "get_weather tool should have been called"

    # Turn 2
    messages.append(HumanMessage(content="How about London?"))
    response2 = agent.invoke({"messages": messages})
    final_message2 = response2["messages"][-1].content

    assert any(location.lower() in final_message2.lower() for location in LOCATIONS)
    assert any(
        pattern.lower() in final_message2.lower() for pattern in TEMPERATURE_UNITS
    )
    assert any(condition.lower() in final_message2.lower() for condition in CONDITIONS)

    get_weather_called = any(
        hasattr(msg, "tool_calls")
        and any(tc.get("name") == TOOL_NAME for tc in msg.tool_calls)
        for msg in response2["messages"]
    )
    assert get_weather_called, "get_weather tool should have been called"


# def test_weather_agent_error_handling():
#     """
#     Scenario Type: Edge Case
#     Scenario: Rate limiting exceeded
#     Prompt: "What's the weather?"
#     Criteria:
#         - Agent must respond with user-friendly error message
#         - Agent must NOT crash or timeout silently
#         - Agent must suggest retry later OR fallback location
#         - Message must contain 'rate' or 'too many requests'
#         - Agent must NOT make up fake weather data
#     """
#     agent = get_ai_weather_agent()

#     messages = [HumanMessage(content="What's the weather in Tokyo?")]
#     response = agent.invoke({"messages": messages})
#     final_message = response["messages"][-1].content

#     has_user_friendly_error_message = any(
#         message.lower() in final_message.lower()
#         for message in USER_FRIENDLY_ERROR_MESSAGE
#     )
#     assert not has_user_friendly_error_message, (
#         "Agent should respond with user-friendly message"
#     )


#     has_rate_limiting_error = any(
#         error.lower() in final_message.lower()
#         for error in RATE_LIMITING_ERRORS
#     )
#     assert has_rate_limiting_error, (
#         "Agent should respond with rate limiting message"
#     )


#     has_fake_weather_data = any(
#         data.lower() in final_message.lower() for data in FAKE_WEATHER_DATA
#     )
#     assert not has_fake_weather_data, "Agent should not make up fake weather data"
# #
