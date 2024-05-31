class Employee:
    def __init__(self, employee_id, name, base_salary, allowances, deductions, bonuses):
        self.employee_id = employee_id
        self.name = name
        self.base_salary = base_salary
        self.allowances = allowances
        self.deductions = deductions
        self.bonuses = bonuses

class Attendance:
    def __init__(self, employee_id, date, in_time, out_time):
        self.employee_id = employee_id
        self.date = date
        self.in_time = in_time
        self.out_time = out_time

class HRMIS:
    def __init__(self):
        self.employees = []
        self.attendance_records = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def mark_attendance(self, attendance):
        self.attendance_records.append(attendance)

    def calculate_salary(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                total_salary = emp.base_salary + emp.allowances + emp.bonuses - emp.deductions
                return total_salary

# Create HRMIS instance
hrmis_system = HRMIS()

# Add employees
employee1 = Employee(1, "John Doe", 50000, 2000, 1000, 500)
employee2 = Employee(2, "Jane Smith", 55000, 2500, 1200, 600)
hrmis_system.add_employee(employee1)
hrmis_system.add_employee(employee2)

# Mark attendance
attendance1 = Attendance(1, "2023-10-26", "09:00 AM", "05:00 PM")
attendance2 = Attendance(2, "2023-10-26", "09:30 AM", "06:00 PM")
hrmis_system.mark_attendance(attendance1)
hrmis_system.mark_attendance(attendance2)

# Calculate salary
employee_id = 2
salary = hrmis_system.calculate_salary(employee_id)
print(f"Salary for employee ID {employee_id}: {salary}")
