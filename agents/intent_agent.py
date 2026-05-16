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

def detect_intent(state: PlannerState) -> PlannerState:
    query = state["user_request"]

    prompt=f"""extract the intent from the following user query:
     1.country
      2.city
       3.budget
        4.interests
         {query}"""
    response = llm.invoke(prompt)
    print("\n intent detection completed")
    print(response.content)

    return {
        **state,
        "messages": state["messages"],
    }
    