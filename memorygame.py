import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
@ask.launch
def new_game():
    welcome_msg = render_template(' Welcome to memory game. Im going to say three numbers for you to repeat backwards. Ready?')
    return question(welcome_msg)
@ask.intent("YesIntent")
def next_round():
    numbers = [randint(0, 9) for _ in range(3)]
    round_msg = render_template('Can you repeat the numbers {{ numbers|join(", ") }} backwards?', numbers=numbers)
    session.attributes['numbers'] = numbers[::-1]  # reverse
    return question(round_msg)
@ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})
def answer(first, second, third):
    winning_numbers = session.attributes['numbers']
    if [first, second, third] == winning_numbers:
        msg = render_template('Good job!')
    else:
        msg = render_template('Sorry, thats the wrong answer.')
    return statement(msg)
if __name__ == '__main__':
    app.run(debug=True)
