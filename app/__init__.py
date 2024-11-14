from flask import Flask, render_template_string
from flasgger import Swagger
from pymongo import MongoClient
from app.routes.user_routes import user_bp
from app.routes.order_routes import order_bp
from app.routes.restaurant_routes import restaurant_bp

from flask_migrate import Migrate
from app.database import db

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    # app.config['DATABASE'] = MongoClient('mongodb://localhost:27017/')['food_delivery_app']
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/food_delivery_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    swagger = Swagger(app)
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(restaurant_bp, url_prefix='/api/restaurants')

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def home():
        return render_template_string('<h1>Welcome to the App!</h1><p>The app is running.</p>')

    return app