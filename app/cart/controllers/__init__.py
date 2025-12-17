from flask import Blueprint

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/view', methods=['GET'])
def view_cart():
 return 'View Cart endpoint'