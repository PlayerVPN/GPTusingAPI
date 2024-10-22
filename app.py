from flask import Flask, request, jsonify
import openai
import logging

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "sk-pju8nmSJnvqRyoRZ3a1GmJWfFZu4-XAIUYmxHbxpLqT3BlbkFJhOJFsD2IO1ncZLvxY3FzbtDvu9pjxLzRdvENT95mYA"

# Enable logging to track issues
logging.basicConfig(level=logging.DEBUG)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("user_input")
        logging.debug(f"User input received: {user_input}")

        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150,
            temperature=0.7,
        )

        message = response.choices[0].text.strip()
        logging.debug(f"AI response: {message}")
        return jsonify({"response": message})
    
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"response": "Error: Could not process the request."}), 500

if __name__ == '__main__':
    app.run(debug=True)
