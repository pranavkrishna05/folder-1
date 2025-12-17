from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import and register blueprints
# from app.auth.controllers import auth_bp
# app.register_blueprint(auth_bp)

# from app.products.controllers import products_bp
# app.register_blueprint(products_bp)

# Additional setup can be added here

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)