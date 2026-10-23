from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/user/<int:id>")   #int converter
def user(id):
    return f"user {id}"

@app.route("/price/<float:amount>")  #float converter
def price(amount):
    return f"price {amount}"

@app.route("/customer/<string:id>")   #string converter
def customer(id):
    return f"customer {id}"

@app.route("/files/<path:file_path>")   #path converter
def files(file_path):
    return file_path

from uuid import UUID

@app.route("/student/<uuid:user_id>")   #uuid converter
def student(user_id):
    return str(user_id)


if __name__ == '__main__':
    app.run(debug = True)