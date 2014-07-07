'''
Created on Jun 27, 2014

@author: magus0219
'''
from unicorn.design.decorator.enum import enum
import unittest

@enum
class EnvironmentType(object):
    PRODUCTION = 1
    STAGE = 2
    TEST = 3


class EnumTest(unittest.TestCase):
    @unittest.expectedFailure    
    def testUnvalidEnvironmentType(self):
        @enum
        class UnvalidEnvironmentType(object):
            PRODUCTION = 1
            STAGE = 2
            TEST = 3
            db = 4
        
    def testEnumContain(self):
        self.assertEqual(True, 'TeST' in EnvironmentType)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEnum']
    unittest.main()
