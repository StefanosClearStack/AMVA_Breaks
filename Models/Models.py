from Database.db import db
from datetime import datetime

class EmployeeModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    breaks = db.relationship('BreakModel', backref='employee', lazy=True)

class BreakModel(db.Model):
    __tablename__ = 'breaks'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)

    def __init__(self, employee_id, start_time=None, end_time=None):
        self.employee_id = employee_id
        if start_time:
            self.start_time = start_time
        if end_time:
            self.end_time = end_time
