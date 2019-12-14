from flask_sqlalchemy import SQLAlchemy
import os

# Instantiate a SQLAlchemy object.
db = SQLAlchemy()

class User(db.Model):
    """Data model for a user"""
     __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    list_id = db.Column(db.Integer,
                       db.ForeignKey('list.id'),
                       nullable=True)
    username = db.Column(db.String(30),
                         nullable=False)
    password = db.Column(db.String(30),
                         nullable=False)
    lst = db.relationship("Lst")




# Connect db to app
def connect_to_db(app,dburi="postgres:///todos"):
    """Connect the database to our Flask app."""
    # Configure to use our database.
    app.config["SQLALCHEMY_DATABASE_URI"] =dburi
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_ECHO"] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print("Connected to DB")