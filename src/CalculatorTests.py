import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_Data = CsvReader('/src/Test_Addition.csv').data
        for row in test_Data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']),int(row['Result']))

    def test_subtraction(self):
        test_Data = CsvReader('/src/Test_Subtract.csv').data
        for row1 in test_Data:
            self.assertEqual(self.calculator.subtract(row1['Value 1'], row1['Value 2']),int(row1['Result']))

    def test_multiply(self):
        test_Data = CsvReader('/src/Test_Multiply.csv').data
        for row in test_Data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_division(self):
        test_Data = CsvReader('/src/Test_Division.csv').data
        for row in test_Data:
            self.assertAlmostEqual(self.calculator.division(row['Value 2'], row['Value 1']), float(row['Result']))

    def test_square(self):
        test_Data = CsvReader('/src/Test_Square.csv').data
        for row in test_Data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))

    def test_squareroot(self):
        test_Data = CsvReader('/src/Test_SquareRoot.csv').data
        for row in test_Data:
            self.assertAlmostEqual(self.calculator.squareroot(row['Value 1']), float(row['Result']))

def test_results_property(self):
    self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()