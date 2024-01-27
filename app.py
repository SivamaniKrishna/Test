from flask import Flask, request, jsonify
import openai

# Initialize your OpenAI API key
openai.api_key = 'your_openai_api_key_here'

app = Flask(__name__)

# Define a route for your Flask app to receive input
@app.route('/ask', methods=['POST'])
def ask_openai():
    # Get the input from the request
    input_text = request.json['input']

    # Call the OpenAI API to get a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=50
    )

    # Extract the response text from the API response
    response_text = response.choices[0].text.strip()

    # Return the response as JSON
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
