from flask import Blueprint

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/overview', methods=['GET'])
def checkout_overview():
 return 'Checkout Overview endpoint'