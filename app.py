from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuring the Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'alahamedbasithce@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'amnbzamsacwumroy'  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = 'alahamedbasithce@gmail.com'

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
                  recipients=['ahamedbasith006@gmail.com'])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    try:
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'message': 'Error sending email'}), 500

if __name__ == '__main__':
    app.run(port=4000)
