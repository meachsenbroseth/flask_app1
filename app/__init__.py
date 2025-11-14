import os
from flask import Flask
from app.main.routes import main_bp
from app.auth.routes import auth_bp

def create_app():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    STATIC_DIR = os.path.join(BASE_DIR, '..', 'static')

    app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

    app.config["SECRET_KEY"] = "change-me"

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app