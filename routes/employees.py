from fastapi import APIRouter
from typing import List
from models import Employee
import crud

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/", response_model=List[Employee])
def list_employees():
    return crud.get_all_employees()

@router.get("/{id}", response_model=Employee)
def get_employee(id: int):
    return crud.get_employee_by_id(id)

@router.post("/", response_model=Employee, status_code=201)
def create_employee(employee: Employee):
    return crud.create_employee(employee)

@router.put("/{id}", response_model=Employee)
def update_employee(id: int, employee: Employee):
    return crud.update_employee(id, employee)

@router.delete("/{id}", status_code=204)
def remove_employee(id: int):
    crud.delete_employee(id)
