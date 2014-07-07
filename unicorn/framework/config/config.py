'''
Created on Jun 26, 2014

@author: magus0219
'''
from unicorn.design.decorator.singleton import singleton
from unicorn.design.decorator.enum import enum
import importlib

class ConfigError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.__class__.__name__ + ':' + self.msg

class PropertyNotFound(ConfigError):
    pass

class ConfigFileNotFound(ConfigError):
    pass

class EvironmentError(ConfigError):
    pass

@enum
class EnvironmentType(object):
    PRODUCTION = 1
    STAGE = 2
    TEST = 3

@singleton
class Configration(object):
    '''
    classdocs
    '''

    def __init__(self, conf_package):
        '''
        Constructor
        '''
        self._data = {}
        
        try:
            self.env = importlib.import_module(conf_package + '.' + 'environment').ENVIRONMENT
            
            if self.env not in EnvironmentType:
                raise EvironmentError("Evironment Value (%s) Error" % self.env)
                
            conf_module = importlib.import_module(conf_package + '.' + 'config_' + self.env.lower())
        
        except ImportError:
            raise ConfigFileNotFound('Module (%s) missed' % (conf_package + '.' + 'environment'))
        
        for prop in conf_module.__dict__:
            if not prop.startswith('__'):
                self._data[prop] = conf_module.__dict__[prop]
    
    def __contains__(self, name):
        return name in self._data
        
    def switch(self, env):
        pass
    
    def getProperty(self, name):
        if name in self._data:
            return self._data[name]
        else:
            raise PropertyNotFound('(%s) not exists in configration' % name)
        
    
    
    
