from sys import path as syspath
import os

def get_self_syspath(pyfile):
    '''
    Get which system path this python file using
    
    @param base: absolute path of python file
    @return: one system path string 
    '''
    for path in syspath:
        if pyfile.startswith(path):
            return path

def get_self_package(pyfile):
    '''
    Get package name of itself
    
    @param pyfile: absolute path of python file
    @return: module name this python file stands for
    '''
    path = get_self_syspath(pyfile)
    package = pyfile[len(path):].split('.')[0].replace(os.sep, '.')
    return package[1:] if package.startswith('.') else package

def search_package(syspath, package, target):
    '''
    Search target package in package path upward , one level per time.
    
    For example, we need search package conf from module a.b.c.d, this 
    function then try to find a.b.c.conf/a.b.conf/a.conf/conf , if the target 
    exists, return the target module name
    
    '''
    modules = package.split('.')
    for i in range(len(modules), 0, -1):
        search_modules = modules[:i - 1] if modules[:i - 1] else []
        target_file = os.sep.join([
                                   syspath,
                                   os.sep.join(search_modules),
                                   os.sep.join([target,'__init__.py'])
                                   ])
        if os.path.exists(target_file):
            search_modules.append(target)
            return '.'.join(search_modules)
    
    return None

def search_package_from_pyfile(pyfile, target):
    '''
    Wrapper function of search_package, use python file path as paramter.
    
    @param pyfile: absolute path of python file
    @param target: target package to search
    @return: package name if found, None else. 
    '''
    return search_package(get_self_syspath(pyfile),
                          get_self_package(pyfile),
                          target)

    
