from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Use your OpenAI API key here
openai.api_key = "sk-pju8nmSJnvqRyoRZ3a1GmJWfFZu4-XAIUYmxHbxpLqT3BlbkFJhOJFsD2IO1ncZLvxY3FzbtDvu9pjxLzRdvENT95mYA"

@app.route('/chat', methods=['POST'])
def chat():
    try:
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
    
    except Exception as e:
        print(f"Error: {e}")  # This prints any errors to the console for debugging
        return jsonify({"response": "Sorry, something went wrong with the AI."})

if __name__ == '__main__':
    app.run(debug=True)
