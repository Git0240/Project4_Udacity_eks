from flask import Flask
# from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    # db.init_app(app)

    # Register blueprints or routes
    from .routes import main
    app.register_blueprint(main)

    return app

APP = create_app()
