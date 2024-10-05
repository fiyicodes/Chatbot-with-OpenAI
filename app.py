from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__, static_url_path='/static')

openai.api_key = "sk-IjyRgsO9-8N9NiB8yAvAIbuvGoKyGCphDMG5HrfMkZT3BlbkFJsURK_pOlUDU7PMUn1oYTlMn-mUDXsBuyYAsBeZV1UA"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    try:
        # Adding context to the chatbot to match Codedatt's tone and theme
        context = "You are a chatbot for Codedatt, an Instagram page focused on programming, coding tips, and technology memes. Please provide informative, helpful, and sometimes witty responses to questions related to coding and tech."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_input}
            ]
        )
        
        ai_message = response['choices'][0]['message']['content'].strip()
        return jsonify({'message': ai_message})
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'message': 'Sorry, something went wrong. Please try again.'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)