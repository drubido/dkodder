from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'cdrr930725@gmail.com',
	MAIL_PASSWORD = 'Matrix3.141592654'
	)
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index-particlas.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    try:
        msg = Message(request.form.get("subject"),
          sender = request.form.get("email"),
          recipients=["cdrr930725@gmail.com"])
        name = request.form.get("name")
        message = request.form.get("message")
        msg.html = render_template("/email.html", name = name, subject = subject, message = message)
        mail.send(msg)
    except Exception as e:
        return str(e)
if __name__ == '__main__':
   app.run()
