'''
Created on Mar 11, 2014

@author: magus0219

Singleton here is written as a decorator for class.

I replace target class's __new__ to check whether it has been created.This 
technique is introduced by Guido van Rossum on his paper at @see: www.python.org/download/releases/2.2.3/descrintro/#__new__.
Further more,I leave a blank __init__ in target class and pass its original
method to a hidden place for called just the first time.
'''
import copy
def singleton(cls):
    cls._init = copy.deepcopy(cls.__init__)
    
    def new(cls, *args, **kwds):
        '''
        Replace __new__ of cls here to confirm only one instance is created. 
        
        '''
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        cls._init(it, *args, **kwds)
        return it
    
    def __init__(self, *args, **kwds):
        '''
        Do nothing here for __init__ will be called every time cls is instanced
        
        '''
        pass
    
    cls.__new__ = staticmethod(new)
    cls.__init__ = __init__
    return cls
    
