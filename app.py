from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/generate_and_send_email', methods=['POST'])
def generate_and_send_email():
    data = request.json
    # Here you would implement your AI email generation logic
    generated_email = generate_email_with_ai(data)
    
    # Send the email using Mailgun
    response = send_simple_message(data['recipient'], data['subject'], generated_email)
    
    return jsonify({"status": "Email sent", "mailgun_response": response.text})

def generate_email_with_ai(data):
    # Implement your AI email generation logic here
    # For now, we'll just return a placeholder
    return f"This is a generated email about {data['subject']}"

def send_simple_message(to, subject, text):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxb679256d861d4771b8fa8d9fdc308e8d.mailgun.org/messages",
        auth=("api", "6a6c73f07ffd0dccfe4f5ee585a2e033-0f1db83d-78882fa4"),
        data={"from": "Excited User <zinabeelah@gmail.com>",
              "to": [to],
              "subject": subject,
              "text": text})

if __name__ == '__main__':
    app.run(debug=True)