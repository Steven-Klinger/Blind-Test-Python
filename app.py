# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class and assign it to the 'app' variable
app = Flask(__name__)

# Define a route for the root URL '/' and define the function to handle requests to this route
@app.route('/')
def index():
    # Return a simple greeting message
    return 'Welcome to the Blind Test WebApp!'

# Define a route for the '/about' URL and define the function to handle requests to this route
@app.route('/about')
def about():
    # Return a simple message about the Blind Test WebApp
    return 'I have to learn code again because i\'m rusty so...why not a blind test??'

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
