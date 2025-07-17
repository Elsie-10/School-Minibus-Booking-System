from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api

# Import db from models package (make sure models/__init__.py defines db = SQLAlchemy())
from models import db

# Import blueprints from routes
from routes.booking_route import booking_bp
from routes.auth_route import registration_bp
from routes.bus_routes import bus_bp
from routes.routes import route_bp

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minibus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Extensions
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)
api = Api(app)

# Register Blueprints with consistent prefixes
app.register_blueprint(booking_bp, url_prefix="/bookings")
app.register_blueprint(registration_bp, url_prefix="/register")
app.register_blueprint(bus_bp, url_prefix="/buses")
app.register_blueprint(route_bp, url_prefix="/routes")

# Main entry point
if __name__ == "__main__":
    app.run(debug=True, port=5000)

