from flask import Blueprint

promotions_bp = Blueprint('promotions', __name__)

@promotions_bp.route('/list', methods=['GET'])
def list_promotions():
 return 'List Promotions endpoint'