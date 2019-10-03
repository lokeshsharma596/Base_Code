import unittest
import Calc

class Testcalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calc.add(10,5),15)
        self.assertEqual(Calc.add(-1,1),0)
        self.assertEqual(Calc.add(0,0),0)
        self.assertEqual(Calc.add(-5,-2),-7)

    def test_subtract(self):
        self.assertEqual(Calc.subtract(3,5),-2)
        self.assertEqual(Calc.subtract(-1,1),-2)
        self.assertEqual(Calc.subtract(0,0),0)
        self.assertEqual(Calc.subtract(5,6),-1) 

    def test_multiply(self):
        self.assertEqual(Calc.multiply(10,5),50)
        self.assertEqual(Calc.multiply(-1,1),-1)
        self.assertEqual(Calc.multiply(10,10),100)
        self.assertEqual(Calc.multiply(-6,0),0)

    def test_divide(self):
        self.assertEqual(Calc.divide(10,5),2)
        self.assertEqual(Calc.divide(-1,1),-1)
        self.assertEqual(Calc.divide(100,10),10)
        self.assertEqual(Calc.divide(-50,-2),25)
        
        with self.assertRaises(ValueError):
            Calc.divide(10, 0)
    

if __name__ == '__main__':
    unittest.main()
