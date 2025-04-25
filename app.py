from flask import Flask, render_template, request
from ollama_client import ask_ollama
from utils import parse_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    title = ""
    code = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = ask_ollama(prompt)
        title, code = parse_response(response)
    return render_template("index.html", title=title, code=code)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
