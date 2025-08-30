import streamlit as st
import requests
import json

st.title("💰 Personal Finance Chatbot")

tab1, tab2 = st.tabs(["Ask", "Budget Summary"])

with tab1:
    question = st.text_input("Ask a finance question:")
    if st.button("Ask"):
        r = requests.post("http://127.0.0.1:8000/ask", json={"question": question})
        st.write(r.json())

with tab2:
    income = st.number_input("Income", value=50000)
    expenses = st.text_area("Expenses (JSON)", '{"rent": 15000, "food": 8000}')
    goal = st.text_input("Savings goal", "Emergency fund")
    if st.button("Get Summary"):
        try:
            exp_dict = json.loads(expenses)
            payload = {"income": income, "expenses": exp_dict, "goal": goal}
            r = requests.post("http://127.0.0.1:8000/budget-summary", json=payload)
            st.write(r.json())
        except Exception as e:
            st.error(str(e))
