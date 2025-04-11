from flask import Flask, request, jsonify
from fastapi import FastAPI
from flask_cors import CORS  # Import CORS
import json
from difflib import get_close_matches


app = FastAPI()
app = Flask(__name__)
CORS(app, origins=["https://cbeabishek.github.io/py-chatbot/"], supports_credentials=True)  # Enable CORS for the specified origin
  # Enable CORS for all routes

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def find_best_match(user_question: str, questions: list) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    knowledge_base = load_knowledge_base('knowledge_base.json')

    best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

    if best_match:
        answer = get_answer_for_question(best_match, knowledge_base)
        return jsonify({'answer': answer})
    else:
        return jsonify({'answer': "I don't know the answer. Can you teach me?"})

@app.route('/teach', methods=['POST'])
def teach():
    user_input = request.json.get('question')
    new_answer = request.json.get('answer')

    knowledge_base = load_knowledge_base('knowledge_base.json')
    knowledge_base["questions"].append({"question": user_input, "answer": new_answer})

    with open('knowledge_base.json', 'w') as file:
        json.dump(knowledge_base, file, indent=2)

    return jsonify({'message': 'Thank you! I learned a new response.'})


if __name__ == '__main__':
    app.run(debug=True)
