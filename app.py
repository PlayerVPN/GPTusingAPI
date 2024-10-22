from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Your OpenAI API key
openai.api_key = "sk-pju8nmSJnvqRyoRZ3a1GmJWfFZu4-XAIUYmxHbxpLqT3BlbkFJhOJFsD2IO1ncZLvxY3FzbtDvu9pjxLzRdvENT95mYA"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("user_input")
    
    if not user_input:
        return jsonify({"response": "Please provide a message."}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150,
            temperature=0.7,
        )
        
        message = response.choices[0].text.strip()
        return jsonify({"response": message})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
