from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
@make_bold
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           ' <p> This is paragraph</p>' \
           '<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif">'

@app.route('/bye')
def bye():
    return 'Bye bye!'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello there is  {name}, you are {number} years old!'


app.run(debug=True)

