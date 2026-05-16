from state.planner_state import PlannerState
from tool.hotel_tool import search_hotels

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

def hotel_agent(state: PlannerState):
    hotels = search_hotels(
        state["city"],
        state["budget"]
    )

    print("\nHotel Recommendations")
    print(hotels)

    return {
        **state,
        "hotels": hotels,
    }