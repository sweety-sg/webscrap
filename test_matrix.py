import unittest
from matrix import matrix

class TestCalc(unittest.TestCase):
    def test_add(self) :
        a= matrix([[1,0],[0,1]])
        b= matrix([[2,0],[0,2]])
        c = matrix([[2,0,0],[1,0,2]])
        ans = matrix([[3,0],[0,3]])
        obtained = a+b
        self.assertEqual(ans.values,obtained.values)
        with self.assertRaises(ValueError) :
            a+c
        # print(ans.values)
        # print(obtained.values)

    def test_sub(self) :
        a= matrix([[1,0],[0,1]])
        b= matrix([[2,0],[0,2]])
        c = matrix([[2,0,0],[1,0,2]])
        ans = matrix([[-1,0],[0,-1]])
        obtained = a-b
        self.assertEqual(ans.values,obtained.values)
        with self.assertRaises(ValueError) :
            a-c

    def test_mul(self) :
        a= matrix([[1,0],[0,1]])
        b= matrix([[2,0],[0,2]])
        ans = b
        obtained = a*b
        self.assertEqual(ans.values,obtained.values)
        c = matrix([[2,0,0],[1,0,2]])
        with self.assertRaises(ValueError) :
            c*a

    def test_det(self) :
        a= matrix([[1,0],[0,1]])
        b= matrix([[2,0],[0,2]])
        c = matrix([[2,0,0],[1,0,2]])
        obtained1 = matrix.__det__(a)
        obtained2 = matrix.__det__(b)
        ans1 = 1
        ans2 = 4
        self.assertEqual(ans1,obtained1)
        self.assertEqual(ans2,obtained2)
        with self.assertRaises(ValueError) :
            matrix.__det__(c)

    def test_pow(self) :
        a1= 5
        a2 = 2
        b= matrix([[2,0],[0,2]])
        ans1 = matrix([[32,0],[0,32]])
        ans2 = matrix([[4,0],[0,4]])
        obtained1 = (b**a1).values.values
        obtained2 = (b**a2).values.values
        # print(ans1)
        # print(obtained1)
        self.assertEqual(ans1.values,obtained1)
        self.assertEqual(ans2.values,obtained2)
        c = matrix([[2,0,0],[1,0,2]])
        with self.assertRaises(ValueError) :
            (c**a1).values.values
            
        



if __name__ == '__main__' :
    unittest.main()
