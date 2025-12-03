from flask import Flask,Blueprint
from flask_cors import CORS

def create_app():
    app=Flask(__name__)
    CORS(app)
    
    from app import score_bp
    app.secret_key = 'your_secret_key'
    app.register_blueprint(score_bp)
    
    return app