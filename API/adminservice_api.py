from flask import Blueprint, request, jsonify
from Services.adminservice import AdminService

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/api/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    result = AdminService.create_employee(username, password)
    return jsonify({"message": result}), 201

@admin_bp.route('/api/employees/<int:employee_id>', methods=['PUT'])
def edit_employee(employee_id):
    data = request.get_json()
    new_username = data.get('username')
    new_password = data.get('password')

    result = AdminService.edit_employee(employee_id, new_username, new_password)
    return jsonify({"message": result}), 200

@admin_bp.route('/api/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    result = AdminService.delete_employee(employee_id)
    return jsonify({"message": result}), 200

@admin_bp.route('/api/employees', methods=['GET'])
def get_all_employees():
    employees = AdminService.get_all_employees()
    employee_list = [{"id": emp.id, "username": emp.username} for emp in employees]
    return jsonify(employee_list), 200

@admin_bp.route('/api/employees/<int:employee_id>', methods=['GET'])
def get_employee_by_id(employee_id):
    employee = AdminService.get_employee_by_id(employee_id)
    if employee:
        return jsonify({"id": employee.id, "username": employee.username}), 200
    else:
        return jsonify({"error": "Employee not found"}), 404
