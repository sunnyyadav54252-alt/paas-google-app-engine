from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! PaaS implementation using Google App Engine via GitHub"

if __name__ == '__main__':
    app.run()
