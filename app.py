from flask import Flask, render_template, request
from openai import OpenAI
import json
import os

app = Flask(__name__)

client = OpenAI()

@app.route('/')
def home_page():
    # key = os.environ.get('OPENAI_API_KEY')
    # return key
    return render_template("index.html")

@app.route('/riddle_bot')
def chat():
    prompt = request.args.get('prompt')
    messages = [{"role":"system", "content":"You are a normal Chatbot assistant, but you speak in cryptic riddles and rhymes."}]
    convo = json.loads(prompt)
    messages.extend(convo)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print(completion.choices[0].message.content)
    return(completion.choices[0].message.content)

if __name__ == '__main__':
    app.run(debug=True)