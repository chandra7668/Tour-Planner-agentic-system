
import os

from state.planner_state import PlannerState
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("gemini_api_key"),
    temperature=0.7
)


def optimize_schedule(state: PlannerState):

    weather = state["weather"]

    if "rain" in weather.lower():
        schedule = "Indoor activities added due to rain"

    else:
        schedule = "Outdoor activities scheduled"

    print("\nSchedule Optimization Completed")

    return {
        **state,
        "optimized_schedule": schedule,
    }