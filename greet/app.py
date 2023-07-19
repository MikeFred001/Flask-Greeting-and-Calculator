from flask import Flask, request

app = Flask(__name__)

@app.get('/welcome/<location>')
def special_greet(location):

    return f"""
        <html>
            <body>
                <h1>
                welcome {location}
                </h1>
            </body>
        <html>
    """

@app.get('/welcome')
def greet():

    return f"""
        <html>
            <body>
                <h1>
                welcome
                </h1>
            </body>
        <html>
    """