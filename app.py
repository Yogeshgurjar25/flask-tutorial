from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Yogesh"
    course = "Python Flask"
    city = "Indore"
    age:22

    return render_template("index.html",
                           name=name,
                           course=course,
                           city=city,
                           age=22)



if __name__ == '__main__':
    app.run(debug = True)