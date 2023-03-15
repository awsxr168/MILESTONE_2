"""Flask application with embedded chatbot and analytics"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'bdqVBWEsRebA4d@GiXm7'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Chatbot(FlaskForm):
    response = StringField('How are you feeling today?',
                           validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    name = None
    instr = "Please proceed to the Chatbot"
    if form.validate_on_submit():
        name = form.name.data
    return render_template('index.html', form=form, name=name, instr=instr)


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    form = Chatbot()
    response = None
    tone = None
    if form.validate_on_submit():
        response = form.response.data
        # positive_responses = ["Great!", "Cool!", "Congratulations!", "Beautiful!", "Good to know!"]
        # negative_responses = ["Too bad!", "Womp, womp!", "Better luck next time!", "Sorry to hear that."]
        # neutral_responses = ["hmmm", "I see"]
        # positive = list(pd.read_csv("positive_words.txt", header=0).iloc[:,0].values)
        # negative = list(pd.read_csv("negative_words.txt", header=0).iloc[:,0].values)
        
        # tone = ""
        # while True:
        #     msg = form.response.data
        #     positive_word_count = len(set(msg.split(" ")).intersection(set(positive)))
        #     negative_word_count = len(set(msg.split(" ")).intersection(set(negative)))
            
        #     if positive_word_count > negative_word_count:
        #         tone = random.choice(positive_responses)

        #     elif negative_word_count > positive_word_count:
        #         tone = random.choice(negative_responses)

        #     else:
        #         tone = random.choice(neutral_responses)

        #     if ("end" in msg) or ("quit" in msg):
        #         break

    # return render_template('chatbot.html', form=form, response=response, tone=tone)
    return render_template('chatbot.html', form=form, response=response)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
