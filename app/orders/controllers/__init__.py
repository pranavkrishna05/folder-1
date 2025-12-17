from flask import Blueprint

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/history', methods=['GET'])
def order_history():
 return 'Order History endpoint'