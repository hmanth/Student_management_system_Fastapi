from fastapi import FastAPI
from pydantic import BaseModel
from database import Base, engine, LocalSession
from models import Employee


api = FastAPI()

Base.metadata.create_all(bind=engine)


# Request model for adding employee
class EmployeeRequest(BaseModel):

    name: str
    department: str
    salary: float


# Request model for updating salary
class SalaryRequest(BaseModel):

    salary: float


# Request model for updating department
class DepartmentRequest(BaseModel):

    department: str


# Home
@api.get("/")
def home():

    return {
        "Message": "Employee Management System API"
    }


# Add employee
@api.post("/employees")
def add_employee(request: EmployeeRequest):

    db = LocalSession()

    employee = Employee(
        name=request.name,
        department=request.department,
        salary=request.salary
    )

    db.add(employee)

    db.commit()

    db.close()

    return {
        "Message": "Employee added successfully"
    }


# View all employees
@api.get("/employees")
def get_employees():

    db = LocalSession()

    employees = db.query(Employee).all()

    db.close()

    return employees


# Search employee by name or department
@api.get("/employees/search")
def search_employees(value: str):

    db = LocalSession()

    employees = db.query(Employee).filter(
        (Employee.name.like("%" + value + "%")) |
        (Employee.department.like("%" + value + "%"))
    ).all()

    db.close()

    return employees


# Search employee by ID
@api.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    db = LocalSession()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    db.close()

    return employee


# Update salary
@api.put("/employees/{employee_id}/salary")
def update_employee_salary(
    employee_id: int,
    request: SalaryRequest
):

    db = LocalSession()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee:

        employee.salary = request.salary

        db.commit()

    db.close()

    return {
        "Message": "Salary updated successfully"
    }


# Update department
@api.put("/employees/{employee_id}/department")
def update_employee_department(
    employee_id: int,
    request: DepartmentRequest
):

    db = LocalSession()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee:

        employee.department = request.department

        db.commit()

    db.close()

    return {
        "Message": "Department updated successfully"
    }


# Delete employee
@api.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    db = LocalSession()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee:

        db.delete(employee)

        db.commit()

    db.close()

    return {
        "Message": "Employee deleted successfully"
    }


# Employee with highest salary
@api.get("/employees/highest-salary")
def highest_salary():

    db = LocalSession()

    employee = db.query(Employee).order_by(
        Employee.salary.desc()
    ).first()

    db.close()

    return employee


# Employee with lowest salary
@api.get("/employees/lowest-salary")
def lowest_salary():

    db = LocalSession()

    employee = db.query(Employee).order_by(
        Employee.salary.asc()
    ).first()

    db.close()

    return employee