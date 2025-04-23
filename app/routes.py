from flask import Blueprint, request, render_template, jsonify
from .emotion_detector import detect_emotion
from .formatter import format_result

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        result = detect_emotion(text)
        formatted = format_result(result)
        return jsonify(formatted)
    return render_template("index.html")
