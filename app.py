from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Abraham Augustine!'

if __name__ == '__main__':
    # Enable debug mode for development purposes
    app.run(debug=True, host='0.0.0.0', port=5000)
