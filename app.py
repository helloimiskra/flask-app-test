from flask import Flask, render_template

app = Flask(__name__)


all_posts = [
    {
        "title": "Post 1",
        "content": "This is the content of post numero uno!"
    },
    {
        "title": "Post 2",
        "content": "This is the content of post numero dos!"
    }
]



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/home/<string:name>')
def hello(name):
    return "Hello, " + name + '.'

@app.route('/onlyget', methods=["GET"]) #allows you to limit methods for routes
def get_req():
    return 'You can only get this webpage.'

if __name__ == "__main__":
    app.run(debug=True)

