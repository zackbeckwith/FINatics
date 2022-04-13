#models 
from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
#allows to set up isAuthenticate etc 
from flask_login import UserMixin
from datetime import datetime

#login management 
# allows us to use this in templates for isUser stuff 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    aquariums = db.relationship('Aquarium', backref='owner', lazy=True)
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return f"Username {self.username}"

class Aquarium(db.Model):
    ___tablename__ = 'aquariums'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(30), default='Aquarium')
    image = db.Column(db.String(36))
    fish = db.Column(db.String(250), nullable=False)
    plants = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(15), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, name, fish, plants, type, user_id, image=None):
        self.name = name
        self.image = image
        self.fish = fish
        self.plants = plants
        self.type = type
        self.user_id = user_id
    
    def __repr__(self):
        return f"Aquarium ID: {self.id} --- Date: {self.date} --- Name: {self.name}"


