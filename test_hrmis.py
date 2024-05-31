import unittest
from employeee import HRMIS, Employee, Attendance 

class HRMISTester(unittest.TestCase):
    def setUp(self):
        self.hrmis = HRMIS()
        emp1 = Employee(1, "Kevin Manzi", "123-456-7890", "Developer", 50000, 2000, 1000, 500)  # Add bonuses to the employee
        att1 = Attendance(1, "2023-10-26", "09:00 AM", "05:00 PM")
        self.hrmis.add_employee(emp1)
        self.hrmis.mark_attendance(att1)

    def test_salary_calculation(self):
           calculated_salary = self.hrmis.calculate_salary(1, 10, 2023)
           self.assertEqual(calculated_salary, 51500, "Incorrect salary calculation") # Update the expected salary

    def test_attendance_marking(self):
        # Assuming the attendance_records list has at least one record
        self.assertTrue(len(self.hrmis.attendance_records) > 0, "Attendance not recorded")

if __name__ == "__main__":
    unittest.main()