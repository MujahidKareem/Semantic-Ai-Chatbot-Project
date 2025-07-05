from transformers import BertTokenizer, BertModel
import torch
import numpy as np
import json
from sklearn.metrics.pairwise import cosine_similarity

# Load intents
with open("intents.json", encoding='utf-8') as f:
    intents = json.load(f)["intents"]


# Load BERT model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Semantic embedder
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

# Create embeddings for patterns
intent_vectors = []
intent_tags = []

for intent in intents:
    for pattern in intent["patterns"]:
        intent_vectors.append(get_embedding(pattern))
        intent_tags.append(intent["tag"])

# Predict intent
def predict_intent(user_input):
    input_vector = get_embedding(user_input)
    similarities = cosine_similarity([input_vector], intent_vectors)
    best_match = np.argmax(similarities)
    confidence = similarities[0][best_match]

    if confidence > 0.7:
        return intent_tags[best_match]
    else:
        return "unknown"
