from typing import TypedDict,List
from langchain_core.messages import HumanMessage,AIMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("gemini_api_key"),
    temperature=0.7
)
class PlannerState(TypedDict):
    messages: List[HumanMessage | AIMessage]
    user_request: str
    city: str
    country: str
    budget: str
    interests: List[str]
    weather: str
    hotels: List[str]
    restaurants: List[str]
    transport: str
    optimized_schedule: str
    itinerary: str
