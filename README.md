
 🤖 NLP-Based Chatbot with Flask & BERT

This project is a "Natural Language Processing (NLP) Chatbot" that semantically analyzes user input and responds intelligently. Built using "Python", "Flask", "BERT tokenizer", and a simple HTML/CSS frontend, it showcases how NLP can be used to build meaningful conversational agents.

---
 🌟 Features

- Intent recognition using custom `intents.json`
- Semantic understanding with BERT tokenizer
- Flask-based backend API
- Simple and clean web interface (HTML + CSS)
- Easily extendable knowledge base (add new intents)

---
 🧠 Technologies Used

| Layer        | Tools & Libraries                    |
|--------------|--------------------------------------|
| Backend      | Python, Flask                        |
| NLP Engine   | BERT Tokenizer (from HuggingFace)    |
| Data Format  | JSON (for intents and responses)     |
| Frontend     | HTML, CSS (Static UI)                |
| ML Support   | TensorFlow (for model integration)   |

---

 📂 Project Structure

```

chatbot\_project/
├── app.py                  # Flask app to serve chatbot
├── chatbot\_model.py        # NLP logic and intent prediction
├── response\_map.py         # Maps predicted intents to responses
├── intents.json            # Custom intent data
├── templates/
│   └── index.html          # Frontend HTML page
├── static/
│   └── style.css           # Chatbot styling
└── README.md               # Project documentation

```

--- 🚀 How to Run the Project

download ZIP and extract it.

2️⃣ Install Required Libraries

Make sure Python is installed. Then run:

```bash
pip install flask
pip install transformers
pip install tensorflow
````

 3️⃣ Run the Flask Server

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

🗂 Sample Intents (`intents.json`)

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hello", "Hi", "Hey there"],
      "responses": ["Hi! How can I assist you today?"]
    },
    {
      "tag": "nlp",
      "patterns": ["What is NLP?", "Tell me about NLP"],
      "responses": ["NLP stands for Natural Language Processing. It's a field of AI that enables computers to understand human language."]
    }
  ]
}
```

---

 🎯 Use Case

This chatbot can be used as:

* A "semester/final year project" for CS students
* A "starting point" for advanced AI-based assistants
* A "demonstration" of NLP intent recognition using BERT

---

 🙌 Credits

Developed by:

* Ai Engineer ( Mujahid Kareem )

---

 📬 Contact

For questions, suggestions, or collaboration:
📧 Email: [mujahidkareem1122@gmail.com)
🔗 LinkedIn: \[https://www.linkedin.com/in/mujahid-kareem-9aa68b308?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app]

---

 📜 License

This project is open source and free to use for educational purposes.

