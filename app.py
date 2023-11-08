from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'You are great,######## Yavor#############!1111WOW!!!!!!!!'
