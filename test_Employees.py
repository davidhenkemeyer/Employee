import unittest
from Employees import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup Class")

    @classmethod
    def tearDownClass(cls):
        print("tearDown Class")

    def setUp(self):
        print("Setup")
        self.emp_1 = Employee("David", "Henkemeyer", 40000)
        self.emp_2 = Employee("Bill", "Johnson", 70000)

    def tearDown(self):
        print("Teardown")
        pass

    def test_email(self):
        print("Test Email")
        self.assertEqual(self.emp_1.email, 'David.Henkemeyer@email.com')
        self.assertEqual(self.emp_2.email, 'Bill.Johnson@email.com')

        self.emp_1.first = "Gabriel"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, 'Gabriel.Henkemeyer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Johnson@email.com')

    def test_fullname(self):
        print("Test Fullname")
        self.assertEqual(self.emp_1.fullname, "David Henkemeyer")
        self.assertEqual(self.emp_2.fullname, "Bill Johnson")

        self.emp_1.first = "Gabriel"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "Gabriel Henkemeyer")
        self.assertEqual(self.emp_2.fullname, "Jane Johnson")

    def test_monthly_schedule(self):
        with patch('Employees.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Henkemeyer/May')
            self.assertEqual(schedule, 'Success')


if __name__ == '__main__':
    unittest.main()


