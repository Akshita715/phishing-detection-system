from flask import Flask, render_template, request
from phishing_detector import analyze_input

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        user_input = request.form.get("user_input")
        result = analyze_input(user_input)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)