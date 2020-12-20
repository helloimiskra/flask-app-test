from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home/<string:name>')

@app.route('/')

def index():
    return render_template('index.html')

def hello(name):
    return "Hello, " + name + '.'

@app.route('/onlyget', methods=["GET"]) #allows you to limit methods for routes
def get_req():
    return 'You can only get this webpage.'

if __name__ == "__main__":
    app.run(debug=True)

