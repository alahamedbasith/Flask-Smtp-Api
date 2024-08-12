from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Configuring the Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Use environment variable
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Use environment variable
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/contact', methods=['GET'])
def contact_get():
    return 'Hello!'

@app.route('/contact', methods=['POST'])
def contact_post():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    print(f"Name: {name}, Email: {email}, Message: {message}")

    msg = Message('Contact Form Submission',
                  recipients=[os.getenv('MAIL_USERNAME')])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    try:
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'message': 'Error sending email'}), 500

if __name__ == '__main__':
    app.run(port=4000)
