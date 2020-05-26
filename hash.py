from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vvwdaonxydwske:e5881cefd23f1bcbd5fbf86423ca9fa606106c93d4e2136efed769608c5ba245@ec2-52-202-22-140.compute-1.amazonaws.com:5432/dci13q0hn8ji3h'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128)) 
    hash = db.Column(db.String(128))

