from flask import Flask, render_template, request
import requests
import os
OPENROUTER_KEY = os.environ.get("OPENROUTER_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", response="")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"]
    result = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openrouter/free",
            "messages": [{"role": "user", "content": question}]
        }
    )
    answer = result.json()["choices"][0]["message"]["content"]
    return render_template("index.html", response=answer)

if __name__ == "__main__":
    app.run(debug=True)
