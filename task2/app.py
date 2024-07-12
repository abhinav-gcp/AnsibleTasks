from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I'm Abhinav! This means my Flask application is working fine and task is completed."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

