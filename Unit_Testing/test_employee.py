import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Lokesh', 'Sharma', 30000)
        self.emp_2 = Employee('Praveen', 'Sharma', 90000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Lokesh.Sharma@gmail.com')
        self.assertEqual(self.emp_2.email, 'Praveen.Sharma@gmail.com')

        self.emp_1.first = 'Luckks'
        self.emp_2.first = 'Ravi'

        self.assertEqual(self.emp_1.email, 'Luckks.Sharma@gmail.com')
        self.assertEqual(self.emp_2.email, 'Ravi.Sharma@gmail.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Lokesh Sharma')
        self.assertEqual(self.emp_2.fullname, 'Praveen Sharma')

        self.emp_1.first = 'Luckks'
        self.emp_2.first = 'Ravi'

        self.assertEqual(self.emp_1.fullname, 'Luckks Sharma')
        self.assertEqual(self.emp_2.fullname, 'Ravi Sharma')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 33000)
        self.assertEqual(self.emp_2.pay, 99000)


if __name__ == '__main__':
    unittest.main()
