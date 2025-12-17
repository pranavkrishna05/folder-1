import os
from flask import Flask


def create_app() -> Flask:
 app = Flask(__name__)
 app.config.from_object('config.Config')

 # Register blueprints
 from app.auth.controllers import auth_bp
 from app.products.controllers import products_bp
 from app.cart.controllers import cart_bp
 from app.checkout.controllers import checkout_bp
 from app.orders.controllers import orders_bp
 from app.reviews.controllers import reviews_bp
 from app.promotions.controllers import promotions_bp
 from app.analytics.controllers import analytics_bp
 from app.customer_support.controllers import customer_support_bp

 app.register_blueprint(auth_bp, url_prefix='/auth')
 app.register_blueprint(products_bp, url_prefix='/products')
 app.register_blueprint(cart_bp, url_prefix='/cart')
 app.register_blueprint(checkout_bp, url_prefix='/checkout')
 app.register_blueprint(orders_bp, url_prefix='/orders')
 app.register_blueprint(reviews_bp, url_prefix='/reviews')
 app.register_blueprint(promotions_bp, url_prefix='/promotions')
 app.register_blueprint(analytics_bp, url_prefix='/analytics')
 app.register_blueprint(customer_support_bp, url_prefix='/customer_support')

 # Initialize logging
 if not os.path.exists('logs'):
 os.mkdir('logs')
 handler = logging.FileHandler('logs/app.log')
 handler.setLevel(logging.INFO)
 app.logger.addHandler(handler)
 app.logger.setLevel(logging.INFO)
 
 app.logger.info('Application startup')

 return app


if __name__ == '__main__':
 app = create_app()
 app.run(host='0.0.0.0', port=5000)