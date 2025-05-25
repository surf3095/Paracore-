from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from models import db
from auth import auth

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)