from __future__ import print_function
from simpleconfigparser import simpleconfigparser

config = simpleconfigparser()
config.read('read.ini')

print(config.app.debug)
print(config.app.getboolean('debug'))
print(config.app.verbose)
print(config.app.getboolean('verbose'))
print(config.app.name)
