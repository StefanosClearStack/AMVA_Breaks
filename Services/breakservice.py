from datetime import datetime
from Database.db import db
from Models.Models import BreakModel, EmployeeModel

class BreakService:

    @staticmethod
    def punch_break(employee_id):
        # Check if the employee exists
        employee = EmployeeModel.query.get(employee_id)
        if not employee:
            return f"Employee with ID '{employee_id}' not found."

        # Check if there is an active break (one without an end time) for the employee
        active_break = BreakModel.query.filter_by(employee_id=employee_id, end_time=None).first()
        if active_break:
            return f"Employee '{employee.username}' is already on a break that has not been ended."

        # Create a new break entry with the current time as the start time
        new_break = BreakModel(employee_id=employee_id, start_time=datetime.utcnow())
        db.session.add(new_break)
        db.session.commit()
        return f"Employee '{employee.username}' started a break at {new_break.start_time}."

    @staticmethod
    def exit_break(employee_id):
        # Check if the employee exists
        employee = EmployeeModel.query.get(employee_id)
        if not employee:
            return f"Employee with ID '{employee_id}' not found."

        # Find the active break (one without an end time)
        active_break = BreakModel.query.filter_by(employee_id=employee_id, end_time=None).first()
        if not active_break:
            return f"No active break found for employee '{employee.username}'."

        # End the break by setting the current time as the end time
        active_break.end_time = datetime.utcnow()
        db.session.commit()
        return f"Employee '{employee.username}' ended their break at {active_break.end_time}."
# Employee starts a break
