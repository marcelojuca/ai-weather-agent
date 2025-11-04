# tests/test_weather_agent.py
import scenario
from agents.weather import get_weather_agent


@scenario.test(
    description="User asks for weather in Tokyo → agent returns current temp & condition",
    agents=[
        scenario.UserSimulatorAgent(),
        scenario.JudgeAgent(
            criteria=[
                "Response includes temperature in °C",
                "Response includes condition (e.g., sunny, rainy)",
                "No hallucinations about future dates",
                "Uses weather API tool correctly",
            ]
        ),
    ],
    max_turns=3,
)
def test_weather_agent():
    result = scenario.run(get_weather_agent())
    assert result.success  # Will fail until agent works
