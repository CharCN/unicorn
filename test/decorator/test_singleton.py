'''
Created on Mar 11, 2014

@author: magus0219
'''
from unicorn.design.decorator.singleton import singleton
import unittest

class SingletonTest(unittest.TestCase):

    def testNormalClass(self):
        @singleton
        class Foo(object):
            def __init__(self, data):
                self.data = data
            
            def __str__(self):
                return self.data
            
        f1 = Foo("data1")
        f2 = Foo("data2")
        
        self.assertEqual("data1", str(f1))
        self.assertEqual("data1", str(f2))
        self.assertEqual(True, f1 is f2)
        
    def testSubClass(self):
        class Foo(object):
            def __init__(self, data):
                self.data = data
            
            def __str__(self):
                return self.data
            
        @singleton   
        class Bar(Foo):
            def __init__(self, data1, data2):
                Foo.__init__(self, data1)
                self.data2 = data2
            
            def __str__(self):
                return "%s,%s" % (self.data, self.data2)
            
        f1 = Bar("aaa", "bbb")
        f2 = Bar("ccc", "ddd")
        
        self.assertEqual("aaa,bbb", str(f1))
        self.assertEqual("aaa,bbb", str(f2))
        self.assertEqual(True, f1 is f2)
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testSingleton']
    unittest.main()
