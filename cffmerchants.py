from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'CFF Merchants is in business'
