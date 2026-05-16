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

def analyze_budget(state:PlannerState):
    budget=state["budget"]
    if budget.lower() == "low":
        recommendation = 'budget hotels and public transport'
    elif budget.lower() == 'medium':
        recommendation = 'mid-range hotels and a mix of public transport and taxis'
    elif budget.lower() == 'high':
        recommendation='luxury hotels and private transportation'
    else:
        recommendation="luxury hotels and cab services"

    print("\n budget analysis completed")

    return {
        **state,"optimized_schedule": recommendation
    }