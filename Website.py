''' Portfolio
Added everything from contact, homepage, to projects'''
from flask import Flask
import nest_asyncio
from werkzeug.serving import run_simple
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from flask import flash
import os
from dotenv import load_dotenv
load_dotenv() 


app = Flask(__name__)

app.secret_key = 'random'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
# Initialize the Mail extension
mail = Mail(app)

@app.route('/')
def home():
    return render_template('Homepage.html')

@app.route('/Projects')
def about():
    return render_template('projects.html')
   



@app.route('/contact', methods=['GET', 'POST'])   #Used GPT for this route, failed to implement the emailing and messaging part
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_body = request.form.get('message')

        msg = Message(
            "New Contact Form Submission",
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=[app.config['MAIL_USERNAME']]
        )
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"

        try:
            mail.send(msg)
            flash("Message sent! Thank you for contacting me.", "success")
        except Exception as e:
            print(e)
            flash("Failed to send message. Please try again later.", "error")

        return redirect(url_for('contact'))

    # This is the GET request: show the form
    return render_template('contact.html')

    
nest_asyncio.apply()
if __name__ == '__main__':
    app.run(debug=True)