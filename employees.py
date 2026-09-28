# from database import connect_mysql

# #Add employee
# def add_employee():
#     name=input("Enter employee name: ")
#     department=input("Enter department: ")
#     salary=float(input("Enter the salary: "))
#     conn,cursor=connect_mysql()
#     query="""
#     insert into employees(name,department,salary)
#     values (%s,%s,%s)
#     """
#     cursor.execute(query,(name,department,salary))
#     conn.connect()
#     conn.close()
#     print("Employee added succesfully")

# #view employees
# def view_employees():
#     conn,cursor=connect_mysql()
#     cursor.execute("select * from employees")
#     employees=cursor.fetchall()
#     for employee in employees:
#         print(employee)
#     conn.close()

# #search employee
# def search_employee():
#     value=input("Enter name or department: ")
#     conn,cursor=connect_mysql()
#     query="""
#     select * from employees
#     where name like %s or department like %s
#     """
#     search_value="%" + value + "%"
#     cursor.execute(query,(search_value,search_value))
#     employees=cursor.fetchall()
#     for employee in employees:
#         print(employee)
#     conn.close()

# #update salary
# def update_salary():
#     employee_id=int(input("Enter employee ID: "))
#     salary=float(input("Enter new salary: "))
#     conn,cursor=connect_mysql()
#     query="""
#     update employees
#     set salary = %s 
#     where id=%s
#     """
#     cursor.execute(query,(salary,employee_id))
#     conn.commit()
#     conn.close()
#     print("Salary updated successfully")

# #update departmemt
# def update_department():
#     employee_id=int(input("Enter employee ID: "))
#     department=input("Enter new department: ")
#     conn,cursor=connect_mysql()
#     query="""
#     update employees
#     set department = %s 
#     where id = %s
#     """
#     cursor.execute(query,(department,employee_id))
#     conn.commit()
#     conn.close()
#     print("Department updated succesfully")

# #delete employee
# def delete_employee():

#     employee_id = int(input("Enter employee ID: "))

#     conn, cursor = connect_mysql()

#     query = "DELETE FROM employees WHERE id = %s"

#     cursor.execute(query, (employee_id,))

#     conn.commit()

#     conn.close()

#     print("Employee deleted successfully")

# #highest salary
# def highest_salary():

#     conn, cursor = connect_mysql()

#     cursor.execute(
#         "SELECT * FROM employees ORDER BY salary DESC LIMIT 1"
#     )

#     employee = cursor.fetchone()

#     print(employee)

#     conn.close()

# #lowest salary
# def lowest_salary():

#     conn, cursor = connect_mysql()

#     cursor.execute(
#         "SELECT * FROM employees ORDER BY salary ASC LIMIT 1"
#     )

#     employee = cursor.fetchone()

#     print(employee)

#     conn.close()

#ORM
from database import LocalSession
from models import Employee


# Add employee
def add_employee_db(name, department, salary):

    db = LocalSession()

    employee = Employee(
        name=name,
        department=department,
        salary=salary
    )

    db.add(employee)

    db.commit()

    db.close()


# View all employees
def view_employees():

    db = LocalSession()

    employees = db.query(Employee).all()

    db.close()

    return employees


# Search employee by name or department
def search_employee(value):

    db = LocalSession()

    employees = db.query(Employee).filter(
        (Employee.name.like("%" + value + "%")) |
        (Employee.department.like("%" + value + "%"))
    ).all()

    db.close()

    return employees


# Search employee by ID
def get_employee_by_id(employee_id):

    db = LocalSession()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    db.close()

    return employee


# Update salary
def update_salary(employee_id, salary):

    db = LocalSession()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee:

        employee.salary = salary

        db.commit()

    db.close()


# Update department
def update_department(employee_id, department):

    db = LocalSession()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee:

        employee.department = department

        db.commit()

    db.close()


# Delete employee
def delete_employee(employee_id):

    db = LocalSession()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee:

        db.delete(employee)

        db.commit()

    db.close()


# Highest salary
def highest_salary():

    db = LocalSession()

    employee = db.query(Employee).order_by(
        Employee.salary.desc()
    ).first()

    db.close()

    return employee


# Lowest salary
def lowest_salary():

    db = LocalSession()

    employee = db.query(Employee).order_by(
        Employee.salary.asc()
    ).first()

    db.close()

    return employee