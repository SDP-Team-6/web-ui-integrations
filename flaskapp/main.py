from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)