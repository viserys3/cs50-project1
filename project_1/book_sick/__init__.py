from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xrwxszehzeword:ea9e4c63344ed8541e5b447a5ba560205305c82521b6988f8f46c7f5466292ef@ec2-174-129-18-98.compute-1.amazonaws.com:5432/dc8u9ot363f2j'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from book_sick import routes
