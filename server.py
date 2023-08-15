from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting(inp):
    g = "hello " + inp
    return g

@app.route("/calculator/add", methods=['POST'])
def add(a,b):
    return a+b

@app.route("/calculator/subtract", methods=['POST'])
def subtract(a,b):
    val = a-b
    return val

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
