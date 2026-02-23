import streamlit as st
import os
from prompts import meal_prompt,fitness_prompt,weekly_prompt
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Health Planner",
    page_icon="💪",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align:center;'> AI Personal Health Planner</h1>
<p style='text-align:center;color:gray;'>Meal Plan • Workout Plan • Weekly Routine</p>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("User Profile")

age = st.sidebar.number_input("Age", 10, 100, 22)
weight = st.sidebar.number_input("Weight (kg)", 30, 200, 70)
height = st.sidebar.number_input("Height (cm)", 120, 220, 170)

activity = st.sidebar.selectbox(
    "Activity Level",
    ["Sedentary", "Light", "Moderate", "Active", "Athlete"]
)

diet = st.sidebar.selectbox(
    "Diet Preference",
    ["Vegetarian", "Vegan", "Non-Vegetarian", "Keto", "Mediterranean"]
)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    ["Weight Loss", "Muscle Gain", "Maintenance", "Fat Loss", "General Fitness"]
)


# ---------------- PROMPTS ----------------


# ---------------- LLM SETUP ----------------
api_key = st.sidebar.text_input("Enter Google API Key", type="password")

def load_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.9,
        google_api_key=api_key
    )


# ---------------- RUN BUTTON ----------------
if st.button(" Generate My Plan", use_container_width=True):

    if not api_key:
        st.error(" Please enter your API Key in sidebar")
        st.stop()

    user_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "activity": activity,
        "diet": diet,
        "goal": goal
    }

    llm = load_llm()

    parallel_chain = RunnableParallel(
        meal_plan=meal_prompt | llm | StrOutputParser(),
        fitness_plan=fitness_prompt | llm | StrOutputParser()
    )

    weekly_chain = weekly_prompt | llm | StrOutputParser()

    with st.spinner(" Generating your personalized health system..."):

        result = parallel_chain.invoke(user_data)

        meal_plan = result["meal_plan"]
        fitness_plan = result["fitness_plan"]

        weekly_plan = weekly_chain.invoke({
            "meal_plan": meal_plan,
            "fitness_plan": fitness_plan
        })

    # ---------------- OUTPUT UI ----------------
    tab1, tab2, tab3 = st.tabs([" Meal Plan", " Workout Plan", " Weekly Schedule"])

    with tab1:
        st.success("Personalized Nutrition Plan")
        st.markdown(meal_plan)

    with tab2:
        st.success("Personalized Fitness Routine")
        st.markdown(fitness_plan)

    with tab3:
        st.success("7-Day Smart Schedule")
        st.markdown(weekly_plan)


# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:gray;'>Built with LangChain + Gemini + Streamlit</p>",
    unsafe_allow_html=True
)