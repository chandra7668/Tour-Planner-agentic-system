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
def generate_itinerary(state: PlannerState):

    prompt = f"""
    Create a complete travel itinerary.

    City: {state['city']}
    Budget: {state['budget']}
    Interests: {state['interests']}
    Weather: {state['weather']}
    Hotels: {state['hotels']}
    Restaurants: {state['restaurants']}
    Transport: {state['transport']}
    Optimization: {state['optimized_schedule']}

    Create a detailed travel plan.
    """

    response = llm.invoke(prompt)

    print("\nFinal Itinerary")
    print(response.content)

    return {
        **state,
        "itinerary": response.content,
    }