from fastapi import HTTPException
from models import Employee
from database import employees_db, employee_counter

employee_counter = len(employees_db)

def get_all_employees():
    return list(employees_db.values())

def get_employee_by_id(emp_id: int):
    if emp_id not in employees_db:
        raise ValueError("Employee not found")
    return employees_db[emp_id]

def create_employee(employee: Employee):
    global employee_counter
    employee.id = employee.id or employee_counter
    if employee.id in employees_db:
        raise ValueError("Employee ID already exists")
    employees_db[employee.id] = employee
    employee_counter = max(employee_counter, employee.id + 1)
    return employee

def update_employee(emp_id: int, updated_employee: Employee):
    if emp_id not in employees_db:
        raise ValueError("Employee not found")
    updated_employee.id = emp_id
    employees_db[emp_id] = updated_employee
    return updated_employee

def delete_employee(emp_id: int):
    if emp_id not in employees_db:
        raise ValueError("Employee not found")
    del employees_db[emp_id]
