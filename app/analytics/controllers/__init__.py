from flask import Blueprint

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/report', methods=['GET'])
def analytics_report():
 return 'Analytics Report endpoint'