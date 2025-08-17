import os

from typing import Dict
from langchain.schema import HumanMessage

from dotenv import load_dotenv

load_dotenv() 

api_key = os.getenv("GOOGLE_API_KEY")

# 🔑 API Key Setup
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment")



from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize your LLM once here (use your actual model and temperature)
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",
    temperature=0.2
)

def get_symptom(state: Dict) -> Dict:
    # In Streamlit UI, input is handled differently; keep for completeness if reused elsewhere
    symptom = state.get("symptom", "")
    state["symptom"] = symptom
    return state

def classify_symptom(state: Dict) -> Dict:
    prompt = (
        "You are a helpful Medical Assistant. Classify the symptom below into one category:\n"
        "- General\n- Emergency \n- Mental health\n"
        f"Symptom : {state['symptom']}\n"
        "Respond only with one word: General, Emergency, or MentalHealth\n"
        "Example: input: I have fever, Output: General"
    )
    response = llm.invoke([HumanMessage(content=prompt)])
    category = response.content.strip()
    state["category"] = category
    return state

def symptom_router(state: Dict) -> str:
    cat = state.get("category", "").lower()
    if "general" in cat:
        return "general"
    elif "emergency" in cat:
        return "emergency"
    elif "mental" in cat:
        return "mental_health"
    else:
        return "general"

def general_node(state: Dict) -> Dict:
    state["answer"] = (
        f"\n✅ Symptom Received: \"{state['symptom']}\"\n\n"
        "This appears to be a general health concern.\n"
        "➡️ Please proceed to the General Ward for consultation."
    )
    return state

def emergency_node(state: Dict) -> Dict:
    state["answer"] = (
        f"\n🚨 Symptom Received: \"{state['symptom']}\"\n\n"
        "This is a medical emergency! Please seek immediate help."
    )
    return state

def mental_health_node(state: Dict) -> Dict:
    state["answer"] = (
        f"\n🌱 Symptom Received: \"{state['symptom']}\"\n\n"
        "This may be a mental health concern. Please consult with our counselor."
    )
    return state

def process_symptom(symptom: str) -> Dict:
    # This function orchestrates the flow for Streamlit UI
    
    state = {"symptom": symptom}
    state = classify_symptom(state)
    category = symptom_router(state)

    if category == "general":
        state = general_node(state)
    elif category == "emergency":
        state = emergency_node(state)
    else:
        state = mental_health_node(state)
    return state
