from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/users")
def users():
    return "users page"

@app.route("/user/<name>")
def user(name):
    return f"hello {name}"

@app.route("/student/<name>/<course>")
def student(name,course):
    return f"{name} is learning {course}"

if __name__ == '__main__':
    app.run(debug = True)