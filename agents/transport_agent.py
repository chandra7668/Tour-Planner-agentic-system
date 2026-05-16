from state.planner_state import PlannerState
from tool.transport_tool import transport_planner
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("gemini_api_key"),
    temperature=0.7
)


def transport_agent(state: PlannerState):
    transport = transport_planner(
        state["city"],
        state["budget"]
    )

    print("\nTransport Suggestions")
    print(transport)

    return {
        **state,
        "transport": transport,
    }