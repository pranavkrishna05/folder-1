from flask import Blueprint

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/submit', methods=['POST'])
def submit_review():
 return 'Submit Review endpoint'