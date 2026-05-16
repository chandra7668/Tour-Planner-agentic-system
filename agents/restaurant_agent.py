from state.planner_state import PlannerState
from tool.restaurant_tool import search_restaurants
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("gemini_api_key"),
    temperature=0.7
)


def restaurant_agent(state: PlannerState):
    restaurants = search_restaurants(
        state["city"],
        state["interests"]
    )

    print("\nRestaurant Recommendations")
    print(restaurants)

    return {
        **state,
        "restaurants": restaurants,
    }