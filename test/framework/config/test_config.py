'''
Created on Jun 26, 2014

@author: magus0219
'''
import unittest
from unicorn.framework.config import conf

print conf.something

class Test(unittest.TestCase):
    

    def testName(self):
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
