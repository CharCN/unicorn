from unicorn.framework.config.config import Configration
import inspect
from unicorn.util.path import search_package_from_pyfile

caller_pyfile = inspect.stack()[1][1]

conf = Configration(search_package_from_pyfile(caller_pyfile,'conf'))
