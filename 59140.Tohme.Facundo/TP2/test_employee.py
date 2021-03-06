import unittest
from employee import Person
from employee import Employee

class TestPerson(unittest.TestCase):
    def test_get_person(self):
        self.name = "Nahuel"
        self.age = 19 
        datosperson = Person.get_person(self)
        self.assertEqual(datosperson, ["Nahuel", 19])

class TestEmployee(unittest.TestCase):
    def test_get_employee(self):
        self.name = "Nahuel"
        self.age = 19 
        self.salary = 3000
        employee = Employee.get_employee(self)
        self.assertEqual(employee, ["Nahuel", 19, 3000])

    def test_pay_tax_pay(self):
        self.name = "Nahuel"
        self.age = 19
        self.salary = 4000
        tax = Employee.pay_tax(self)
        self.assertEqual(tax, "Paga impuestos")

    def test_pay_tax_no_pay(self):
        self.name = "Carlos"
        self.age = 19
        self.salary = 2000
        notax = Employee.pay_tax(self)
        self.assertEqual(notax, "No paga impuestos")


if __name__ == "__main__":
    unittest.main()
