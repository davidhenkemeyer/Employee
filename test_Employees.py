import unittest
from Employees import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("Setup")
        self.emp_1 = Employee("David", "Henkemeyer", 40000)
        self.emp_2 = Employee("Bill", "Johnson", 70000)

    def tearDown(self):
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

if __name__ == '__main__':
    unittest.main()


