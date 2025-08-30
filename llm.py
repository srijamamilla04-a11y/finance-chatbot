# Placeholder for LLM integration
from transformers import AutoTokenizer, AutoModel
import torch
from config import HF_TOKEN

MODEL_ID = "ibm-granite/granite-embedding-english-r2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=HF_TOKEN)
model = AutoModel.from_pretrained(MODEL_ID, token=HF_TOKEN)

def get_embedding(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()
    return embeddings.numpy()
