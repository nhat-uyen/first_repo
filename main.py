from flask import Flask, request
import random

app = Flask(__name__)

@app.get('/')
def home():
    random_number = None
    
    # Generate random number when form is submitted
    random_number = random.randint(1, 100)
    
    # Create a simple HTML page with a button to generate a random number
    html = ('<h2>Refresh the page to generate a random number between 1 and 100:</h2>'
        f'<h3>{random_number}</h3>'
    )

    return html

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081)
