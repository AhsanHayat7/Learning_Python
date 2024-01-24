from flask import Flask       # Flask is a web framework for Python.
from flask import jsonify     # jsonify is a function provided by Flask to create JSON responses.
    

app = Flask(__name__)    #  Initializes a Flask application.


@app.route('/')
def hello():      # Decorates the hello function to be called when the root URL ("/") is accessed.
    d = {'King':"Lion", 'Sea King': 'Whale', 'Sky King': 'Eagle'} 
    message = {        #  Creates a dictionary message containing status information and a dictionary of scores (d).                      
        'status': 200,   # This is a mock response that you might replace with actual data or logic in a real application.          
        'message': 'OK',                    
        'scores': d
    }
    resp = jsonify(message)  # Uses Flask's jsonify function to convert the message dictionary into a JSON response.
    print(type(resp))        # Prints the type of the resp object and the actual JSON response.
    resp.status_code = 200   # Sets the HTTP status code for the response to 200 (OK).
    print(resp)
    return resp               # Returns the JSON response to the client.


if __name__ == '__main__':
    app.run()


# Runs the Flask application when the script is executed directly.
# Flask starts a development server, and you can access the API at http://127.0.0.1:5000/ (by default). 
# The API response will be a JSON object containing the status, message, and scores.    