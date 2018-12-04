from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index-particlas.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")
    return render_template("email.html", name = name, subject = subject, message = message)

@app.route("/email")
def email():
    return render_template("contact.html")

if __name__ == '__main__':
   app.run(debug = True)
