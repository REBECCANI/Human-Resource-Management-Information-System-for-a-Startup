import json

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
        data = {
            'employees': [emp.__dict__ for emp in self.employees],
            'attendance_records': [att.__dict__ for att in self.attendance_records],
            'salary_records': [sal.__dict__ for sal in self.salary_records]
        }

        with open('hrmis_data.json', 'w') as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open('hrmis_data.json', 'r') as file:
                data = json.load(file)
                self.employees = [Employee(**emp_data) for emp_data in data['employees']]
                self.attendance_records = [Attendance(**att_data) for att_data in data['attendance_records']]
                self.salary_records = [Salary(**sal_data) for sal_data in data['salary_records']]
        except FileNotFoundError:
            print("Data file not found. Initializing empty records.")
            # Initialize empty records or take other appropriate actions based on your requirements
            self.employees = []
            self.attendance_records = []
            self.salary_records = []
        except json.JSONDecodeError:
            print("Error decoding JSON data. Initializing empty records.")
            # Handle JSON decoding error, such as corrupted data, by initializing empty records
            self.employees = []
            self.attendance_records = []
            self.salary_records = []


# Create an instance of HRMIS
hrmis_system = HRMIS()

# Add employees
employee1 = Employee(1, "John Doe", "123-456-7890", "Manager", 50000, 2000, 1000, 500)
employee2 = Employee(2, "Jane Smith", "987-654-3210", "Developer", 55000, 2500, 1200, 600)
hrmis_system.add_employee(employee1)
hrmis_system.add_employee(employee2)

# Mark attendance
attendance1 = Attendance(1, "2023-10-26", "09:00 AM", "05:00 PM")
attendance2 = Attendance(2, "2023-10-26", "09:30 AM", "06:00 PM")
hrmis_system.mark_attendance(attendance1)
hrmis_system.mark_attendance(attendance2)

# Calculate salary
employee_id = 1
month = 10
year = 2023
salary = hrmis_system.calculate_salary(employee_id, month, year)
print(f"Salary for employee ID {employee_id} in {month}/{year}: {salary}")

# Save data to a file
hrmis_system.save_data()

# Load data from the file
hrmis_system.load_data()

# Print loaded data
print("Loaded employees:")
for emp in hrmis_system.employees:
    print(emp.__dict__)

print("Loaded attendance records:")
for att in hrmis_system.attendance_records:
    print(att.__dict__)

print("Loaded salary records:")
for sal in hrmis_system.salary_records:
    print(sal.__dict__)
