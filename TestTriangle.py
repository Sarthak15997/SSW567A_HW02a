# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: Sarthak Vaidya
"""

import unittest
from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Test to check if triangle is a right triangle
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    # Test to check if triangle is a right triangle
    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    # Test to check if triangle is an equilateral triangle
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    # Test to check upper limit of sides of triangle
    def testUpperLimit(self):
        self.assertEqual(classifyTriangle(308, 407, 534), 'InvalidInput', '308, 407, 534 are invalid inputs')

    # Test to check lower limit of sides of triangle
    def testLowerLimit(self):
        self.assertEqual(classifyTriangle(-7, -15, -22), 'InvalidInput', '-7, -15, -22 are invalid inputs')

    # Test to check if given sides do not form a triangle
    def testIfTriangle(self):
        self.assertEqual(classifyTriangle(1, 4, 5), 'NotATriangle', '1, 4, 5 should not be a triangle')

    # Test to check if the given triangle is an isosceles triangle
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(6, 6, 5), 'Isosceles', '6,6,5 should be isosceles')

    # Test to check if the given triangle is an isosceles triangle
    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(5, 7, 7), 'Isosceles', '5,7,7 should be isosceles')

    # Test to check if the given triangle is a scalene triangle
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(7, 9, 11), 'Scalene', '7, 9, 11 should be scalene')

    # Test to check if string input for sides of a triangle is valid
    def testStringTriangle(self):
        self.assertEqual(classifyTriangle('a', 'b', 'c'), 'InvalidInput', 'String inputs should be invalid')

    # Test to check if float input for sides of a triangle is valid
    def testFloatTriangle(self):
        self.assertEqual(classifyTriangle(5.2, 3.5, 8.9), 'InvalidInput', 'Float inputs should be invalid')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
