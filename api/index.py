from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

EMAIL = "tjoeun.jr5@gmail.com"
PASSWORD = "ssqs zvjg sesn cvsn"

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""

    if request.method == 'POST':
        to_email = request.form['to_email']
        subject = request.form['subject']
        body = request.form['body']

        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(EMAIL, PASSWORD)
                server.send_message(msg)

            message = "메일 전송 성공!"
        except Exception as e:
            message = f"에러: {e}"

    return render_template('index.html', message=message)

# ⭐ Vercel용
def handler(request, context):
    return app(request.environ, lambda status, headers: None)
