from datetime import datetime
from book_sick import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    reviews = db.relationship('Review', backref='author', lazy=True)

    def __repr__(self):
        return "User('%s','%s','%s')"%(self.email ,self.username ,self.image_file)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    book_name=db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    posted_by = db.Column(db.String(100),nullable=False,default="Anonymous")

    def __repr__(self):
        return "Post('%s','%s')"%(self.title,self.date_posted)


class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    isbn=db.Column(db.String(25))
    name=db.Column(db.String(100),nullable=False)
    author=db.Column(db.String(100),nullable=False,default='Anonymous')
    release_date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return "Post('%s','%s')"%(self.name,self.author)
