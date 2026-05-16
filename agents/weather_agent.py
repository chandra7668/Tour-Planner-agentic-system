from state.planner_state import PlannerState
from tool.weather_tool import get_weather
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("gemini_api_key"),
    temperature=0.7
)


def weather_agent(state: PlannerState):
    city = state["city"]

    weather = get_weather(city)

    print("\nWeather Information")
    print(weather)

    return {
        **state,
        "weather": weather,
    }