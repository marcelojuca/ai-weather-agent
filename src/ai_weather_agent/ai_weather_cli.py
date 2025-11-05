"""Console script for ai_wheather_agent."""

import typer
from rich.console import Console

from ai_weather_agent import ai_weather_utils

app = typer.Typer()
console = Console()


@app.command()
def main(location: str = typer.Argument("Tokyo", help="Location to get weather for")):
    """Get weather information for a location."""
    report = ai_weather_utils.format_weather_report(location)
    console.print(report)


if __name__ == "__main__":
    app()
