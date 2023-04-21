#Database model
from flask_login import LoginManager, UserMixin
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    #primary key is like a unique identifier for each row
    id = db.Column(db.Integer, primary_key=True)
    #Size (32), nullable is to see if the column is empty or not. false means can't be empty
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    #each function inside of a database has to have self parameter
    def __repr__(self):
        return f'<user {self.id}: {self.username}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
