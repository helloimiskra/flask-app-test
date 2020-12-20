from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False) #nullable means field is required
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False, default="N/A") #strings need character limit
    date_posted = db.Column(db.DateTime, nullable=False, default= datetime.utcnow) #remember to import datetime to use this

    def __repr__(self):
        return "Blog post " + str(self.id)

# all_posts = [
#     {
#         "title": "Post 1",
#         "content": "This is the content of post numero uno!",
#         "author": "Iskra"
#     },
#     {
#         "title": "Post 2",
#         "content": "This is the content of post numero dos!"
#     }
# ]



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=["GET", "POST"])
def posts():
    if request.method=="POST":
        post_title = request.form["title"]
        post_content = request.form["content"]
        new_post = BlogPost(title=post_title, content=post_content, author='Iskra')
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/home/<string:name>')
def hello(name):
    return "Hello, " + name + '.'

@app.route('/onlyget', methods=["GET"]) #allows you to limit methods for routes
def get_req():
    return 'You can only get this webpage.'

if __name__ == "__main__":
    app.run(debug=True)

