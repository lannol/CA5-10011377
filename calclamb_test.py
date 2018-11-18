# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 16:00:00 2018

@author: Olivia
"""

import unittest
from calclamb import add, subtract, divide, multiply, square

class CalculatorTest(unittest.TestCase):
        
    def testAdd(self):
        self.assertEqual(10, add(5,5))
        self.assertEqual(66, add(25,41))
        self.assertEqual(101, add(51,50))
       
    def testSubtract(self):
        self.assertEqual(15, subtract(25, 10))
        self.assertEqual(5, subtract(50, 45))
        
    def testDivide(self):
        self.assertEqual(5, divide(50, 10))
        self.assertEqual(50, divide(150, 3))
        
    def testMultiply(self):
        self.assertEqual(220, multiply(22, 10))
           
    def testSquare(self):
        self.assertEqual(1, square(1))
        self.assertEqual(9, square(3))
        self.assertEqual(25, square(5))
       
unittest.main()
        