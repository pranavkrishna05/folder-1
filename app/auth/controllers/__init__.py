from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
 return 'Login endpoint'

@auth_bp.route('/logout', methods=['POST'])
def logout():
 return 'Logout endpoint'