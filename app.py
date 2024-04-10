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

@app.route('/cryptic_bot')
def cryptic_bot():
    return render_template("cryptic_bot.html")

@app.route('/pirate_bot')
def pirate_bot():
    return render_template("pirate_bot.html")

@app.route('/chat')
def chat():
    prompt = request.args.get('prompt')
    convo = json.loads(prompt)



    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=convo
    )
    print(completion.choices[0].message.content)
    return(completion.choices[0].message.content)

if __name__ == '__main__':
    app.run(debug=True)