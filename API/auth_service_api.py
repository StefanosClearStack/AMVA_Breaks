from flask import Blueprint, request, jsonify
from Services.auth_service import AuthService

# Define the API blueprint
auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    try:
        result = AuthService.login(username, password)
        return jsonify({"message": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
