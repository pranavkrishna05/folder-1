from flask import Blueprint

products_bp = Blueprint('products', __name__)

@products_bp.route('/list', methods=['GET'])
def list_products():
 return 'List Products endpoint'