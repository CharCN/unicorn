'''
Created on Jun 27, 2014

@author: magus0219
'''
import unittest


class EnvironmentType(object):
    PRODUCTION = 1
    STAGE = 2
    TEST = 3
    
    index = {1:"PRODUCT",2:"STAGE",3:"TEST"}
    
    def __prep__(self):
        str = "Enums of %s"(self.__class__)
        return str


class EnumTest(unittest.TestCase):

    def testEnum(self):
        self.assertEqual(1, EnvironmentType.PRODUCTION)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEnum']
    print EnvironmentType
    unittest.main()
