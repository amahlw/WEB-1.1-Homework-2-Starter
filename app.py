from flask import Flask, request, render_template
import random

app = Flask(__name__)


def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')


@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        What is youre favorite toppings?
        <input type="text" name="toppings">
        <input type="submit" value="Submit!">

    </form>
    """


@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} with {users_froyo_toppings} Fro-Yo!'


@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorite_results" method="GET">
        What is your favorite color? <br/>
        <input type="textbox" name="color"><br/>
        What is youre favorite animal?
        <input type="text" name="animal">
        What is youre favorite city?
        <input type="text" name="city">
        <input type="submit" value="Submit!">

    </form>
    """


@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""

    users_favorites_color = request.args.get('color')
    users_favorites_animal = request.args.get('animal')
    users_favorites_city = request.args.get('city')
    return f'Wow, I didnt know {users_favorites_color} {users_favorites_animal} lived in {users_favorites_city}!'


@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
    What's your main secret ? <br/>
    <input type="text" name="message">
    <br/>  <br/>
    <input type="submit" value="Submit">
    </form>
    """


@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_secret_message = request.form.get('message')
    sorted_message = sort_letters(users_secret_message)

    return f"this is your {sorted_message}!"


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template("calculator_form.html")


@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    operand1 = int(request.args.get("operand1"))
    operand2 = int(request.args.get("operand2"))
    operation = request.args.get("operation")
    results = 0

    if operation == "add":
        results = operand1 + operand2
    elif operation == "subtract":
        results = operand1 - operand2
    elif operation == "divide":
        results = operand1 / operand2
    elif operation == "multiply":
        results = operand1 * operand2

    context = {
        "operand1": operand1,
        "operand2": operand2,
        "results": results,
        "operation": operation
    }

    return render_template("calculator_results.html", **context)


# List of compliments to be used in the `compliments_results` route (feel free
# to add your own!)
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]


@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')


@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
