def build_prompt(income, expenses, goal, persona="student"):
    return f"""You are a financial assistant for a {persona}.
Income: {income}
Expenses: {expenses}
Goal: {goal}
Provide a budget summary and recommendations."""
