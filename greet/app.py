from flask import Flask, request

app = Flask(__name__)

@app.get('/welcome/<location>')
def greet(location):
    return f""""
        <html>
            <body>
                <h1>
                welcome {location}
                </h1>
            </body>
        <html>
    """

