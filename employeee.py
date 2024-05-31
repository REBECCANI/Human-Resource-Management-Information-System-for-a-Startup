import pickle

class Employee:
    def __init__(self, employee_id, name, contact_info, role, base_salary, allowances, deductions, bonuses):
        self.employee_id = employee_id
        self.name = name
        self.contact_info = contact_info
        self.role = role
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

class Salary:
    def __init__(self, employee_id, base_salary, allowances, bonuses, deductions):
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.allowances = allowances
        self.bonuses = bonuses
        self.deductions = deductions

class HRMIS:
    def __init__(self):
        self.employees = []
        self.attendance_records = []
        self.salary_records = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def mark_attendance(self, attendance):
        self.attendance_records.append(attendance)

    def calculate_salary(self, employee_id, month, year):
        base_salary = 0
        allowances = 0
        deductions = 0
        bonuses = 0

        for emp in self.employees:
            if emp.employee_id == employee_id:
                base_salary = emp.base_salary
                allowances = emp.allowances
                deductions = emp.deductions
                bonuses = emp.bonuses

        total_salary = base_salary + allowances + bonuses - deductions
        return total_salary

    def save_data(self):
        with open('hrmis_data.pkl', 'wb') as file:
            data = {
                'employees': self.employees,
                'attendance_records': self.attendance_records,
                'salary_records': self.salary_records
            }
            pickle.dump(data, file)

    def load_data(self):
        try:
            with open('hrmis_data.pkl', 'rb') as file:
                data = pickle.load(file)
                self.employees = data['employees']
                self.attendance_records = data['attendance_records']
                self.salary_records = data['salary_records']
        except FileNotFoundError:
            # Handle the case where the data file doesn't exist yet
            pass