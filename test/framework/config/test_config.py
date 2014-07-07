'''
Created on Jun 26, 2014

@author: magus0219
'''
import unittest
from unicorn.framework.config import conf

class ConfigTest(unittest.TestCase):
    
    def testProperty(self):
        self.assertEqual(123, conf.getProperty('SOMETHING_TEST'))
        
    def testContain(self):
        self.assertEqual(False, 'Something' in conf)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
