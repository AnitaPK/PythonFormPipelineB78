from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "title": "Flask + Jenkins for Batch 78",
        "message": "Flask app with templates running successfully!!!!",
        "status": "OKs"
    }
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
