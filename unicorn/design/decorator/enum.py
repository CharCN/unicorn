'''
Created on Jun 27, 2014

@author: magus0219

This module export decorator enum to convert a normal class to a enum class we
defined.Here the key magic is the __metaclass__ of python.

The capacity of enum class we support:
1.Check all enum values should be upper case
2.Provide __iter__ to support iterable
3.Provide __contains__ to support enum label exist check
'''
class EnumError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.__class__.__name__ + ':' + self.msg
    
class EnumMetaClass(type):
    def __new__(cls, name, bases, dct):
        # Here upper all attributes
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        dict_attr = dict((name, value) for name, value in attrs)
        
        # Check UpperCase
        for label,value in dict_attr.items():
            try:
                assert label.isupper()
            except AssertionError:
                raise EnumError("Enum label (%s) can not be lower case."%label)
        
        newtype = type.__new__(cls, name, bases, dict_attr)
        # Here add __enum_strs__ for __iter__
        newtype.__enum_strs__ = dict_attr.keys()
        return newtype
        
    def __iter__(self):
        return iter(self.__enum_strs__)
    
    def __contains__(self,item):
        return item.upper() in self.__enum_strs__

print 123222222
def enum(cls):
    # Just wrapper class using EnumMetaClass 
    cls = EnumMetaClass(cls.__name__,cls.__bases__,cls.__dict__)
    return cls
        