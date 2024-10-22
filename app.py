from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Directly include your API key (not recommended for production)
openai.api_key = "sk-pju8nmSJnvqRyoRZ3a1GmJWfFZu4-XAIUYmxHbxpLqT3BlbkFJhOJFsD2IO1ncZLvxY3FzbtDvu9pjxLzRdvENT95mYA"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("user_input")

    # Call OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can also use 'gpt-4' if available
        prompt=user_input,
        max_tokens=150,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return jsonify({"response": message})

if __name__ == '__main__':
    app.run(debug=True)
