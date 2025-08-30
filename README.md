# Finance Chatbot Project

This project is a basic architecture for a Generative AI based Personal Finance Chatbot.

## Structure
- backend/ : FastAPI app with API endpoints
- frontend/ : Streamlit app for UI
- models/ : Model wrappers (embeddings, LLMs)
- utils/ : Prompt builders, validators
- data/ : Example finance data
- tests/ : Unit tests
- docs/ : Documentation

## Run
1. Install requirements: `pip install -r requirements.txt`
2. Run API: `uvicorn backend.main:app --reload`
3. Run frontend: `streamlit run frontend/app.py`
