from langgraph.graph import StateGraph, END

from state.planner_state import PlannerState

from agents.intent_agent import detect_intent
from agents.budget import analyze_budget
from agents.weather_agent import weather_agent
from agents.hotel_agent import hotel_agent
from agents.restaurant_agent import restaurant_agent
from agents.transport_agent import transport_agent
from agents.optimizer_agent import optimize_schedule
from agents.itinerary_agent import generate_itinerary
workflow = StateGraph(PlannerState)

workflow.add_node("intent_detection", detect_intent)
workflow.add_node("budget_analysis", analyze_budget)
workflow.add_node("weather_agent", weather_agent)
workflow.add_node("hotel_agent", hotel_agent)
workflow.add_node("restaurant_agent", restaurant_agent)
workflow.add_node("transport_agent", transport_agent)
workflow.add_node("optimizer_agent", optimize_schedule)
workflow.add_node("itinerary_agent", generate_itinerary)

workflow.set_entry_point("intent_detection")

workflow.add_edge("intent_detection", "budget_analysis")
workflow.add_edge("budget_analysis", "weather_agent")
workflow.add_edge("weather_agent", "hotel_agent")
workflow.add_edge("hotel_agent", "restaurant_agent")
workflow.add_edge("restaurant_agent", "transport_agent")
workflow.add_edge("transport_agent", "optimizer_agent")
workflow.add_edge("optimizer_agent", "itinerary_agent")
workflow.add_edge("itinerary_agent", END)

app = workflow.compile()