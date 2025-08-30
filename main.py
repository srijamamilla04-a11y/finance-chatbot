from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Finance Chatbot")

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    # Placeholder logic
    return {"answer": f"You asked: {query.question}"}

class Budget(BaseModel):
    income: float
    expenses: Dict[str, float]
    goal: str

@app.post("/budget-summary")
def budget_summary(budget: Budget):
    # Placeholder budget summary
    total_expenses = sum(budget.expenses.values())
    savings = budget.income - total_expenses
    return {
        "income": budget.income,
        "expenses": budget.expenses,
        "goal": budget.goal,
        "savings": savings
    }
