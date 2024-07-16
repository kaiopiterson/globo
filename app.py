import logging
from flask import Flask
from config import Config
from api import api_bp, db

logging.basicConfig(level=logging.DEBUG)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    logging.debug('Initializing SQLAlchemy')
    db.init_app(app)

    logging.debug('Registering Blueprints')
    app.register_blueprint(api_bp)

    return app

if __name__ == '__main__':
    logging.debug('Starting application')
    app = create_app()
    with app.app_context():
        logging.debug('Creating database tables')
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
