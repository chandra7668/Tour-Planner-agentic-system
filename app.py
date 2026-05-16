import os
from dotenv import load_dotenv

load_dotenv()

# Ensure Gemini API key is present before initializing agents
if not os.getenv("gemini_api_key"):
    raise RuntimeError("Missing gemini_api_key in .env — please set it before running the app")

from graph.workflow import app
from langchain_core.messages import HumanMessage


print("Welcome to the Travel Planner!")
user_request = input("Describe your travel request: ")
city = input("Enter city: ")
country = input("Enter country: ")
budget = input("Enter budget (low/medium/high): ")
interests_input = input("Enter interests (comma-separated, e.g., anime,food): ")
interests = [i.strip() for i in interests_input.split(",") if i.strip()]

state = {
    "messages": [],
    "user_request": user_request,
    "city": city,
    "country": country,
    "budget": budget,
    "interests": interests,
    "weather": "",
    "hotels": [],
    "restaurants": [],
    "transport": [],
    "optimized_schedule": "",
    "itinerary": "",
}


for output in app.stream(state):
    pass