from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hellow_world'

@app.route("/about")
def about():
    name = "Shirali"
    location = "Tampa"

    return f"My name is {name}, and I live in {location}."

@app.route("/sum")
def sum():
    x =5
    y =6
    return str(x+y)   

if __name__ == '__main__':
    app.run()

