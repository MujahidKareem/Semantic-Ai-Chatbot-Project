import json
import random

with open("intents.json", encoding="utf-8") as f:
    intents = json.load(f)["intents"]


def get_response(intent_tag):
    for intent in intents:
        if intent["tag"] == intent_tag:
            return random.choice(intent["responses"])
    return "I'm not sure how to respond to that."
