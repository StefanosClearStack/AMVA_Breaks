from Database.db import db
from Models.Models import EmployeeModel, BreakModel  # Ensure this import matches the location of your models

class AdminService:

    def create_employee(username, password):
        # Check if the username already exists
        existing_employee = EmployeeModel.query.filter_by(username=username).first()
        if existing_employee:
            return f"Employee with username '{username}' already exists."
        
        # Create a new employee
        new_employee = EmployeeModel(username=username, password=password)
        db.session.add(new_employee)
        db.session.commit()
        return f"Employee '{username}' created successfully."

    def edit_employee(employee_id, new_username=None, new_password=None):
        # Retrieve the employee by ID
        employee = EmployeeModel.query.get(employee_id)
        if not employee:
            return f"Employee with ID '{employee_id}' not found."

        # Update employee details
        if new_username:
            employee.username = new_username
        if new_password:
            employee.password = new_password
        
        db.session.commit()
        return f"Employee '{employee_id}' updated successfully."

    
    def delete_employee(employee_id):
        # Retrieve the employee by ID
        employee = EmployeeModel.query.get(employee_id)
        if not employee:
            return f"Employee with ID '{employee_id}' not found."
        
        # Delete the employee
        db.session.delete(employee)
        db.session.commit()
        return f"Employee '{employee_id}' deleted successfully."

    def get_all_employees():
        # Retrieve all employees
        employees = EmployeeModel.query.all()
        return employees  # Returns a list of all employee objects

    def get_employee_by_id(employee_id):
        # Retrieve employee by ID
        employee = EmployeeModel.query.get(employee_id)
        return employee  # Returns the employee object if found, otherwise None
