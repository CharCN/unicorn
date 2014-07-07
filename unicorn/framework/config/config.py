'''
Created on Jun 26, 2014

@author: magus0219
'''
from unicorn.design.decorator.singleton import singleton
import importlib

class ConfigError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.__class__.__name__ + ':' + self.msg

class ConfigNotFound(ConfigError):
    pass

class ConfigFileNotFound(ConfigError):
    pass

class EvironmentError(ConfigError):
    pass


class EnvironmentType(object):
    PRODUCTION = 1
    STAGE = 2
    TEST = 3
    
    _enum_strs= ['PRODUCTION','STAGE','TEST']
    
    @staticmethod
    def __contains__(self,item):
        return item in self._enum_strs
    
@singleton
class Configration(object):
    '''
    classdocs
    '''

    def __init__(self, conf_package):
        '''
        Constructor
        '''
        self.data = {}
        
        try:
            self.env = importlib.import_module(conf_package + '.' + 'environment').ENVIRONMENT
            
            print EnvironmentType.__class__.__dict__
        
            if self.env not in EnvironmentType:
                raise EvironmentError("Evironment Value (%s) Error"%self.env)
                
            conf_module = importlib.import_module(conf_package + '.' + 'config_' + self.env.lower())
        
        except ImportError:
            raise ConfigFileNotFound('Module (%s) missed'%(conf_package + '.' + 'environment'))
        
        for prop in conf_module.__dict__:
            if not prop.startswith('__'):
                self.data[prop] = conf_module.__dict__[prop]
        
    def switch(self, env):
        pass
    
    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise ConfigNotFound('(%s) not exists in configration'%name)
        
    
    
    
