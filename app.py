from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Fashion-themed jokes
jokes = [
    "Why did the scarf get promoted? It was outstanding in its field of fashion!",
    "Why did the belt go to school? To hold up its grades!",
    "Why do not fashion designers ever get lost? They always follow the runway!",
    "I tried on a pair of shoes that were too tight… it was a sole crushing experience!",
    "Why did the dress go to therapy? It had too many hang-ups!"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/joke")
def get_joke():
    return jsonify({"joke": random.choice(jokes)})

if __name__ == "__main__":
    app.run(debug=True)
