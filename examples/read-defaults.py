from __future__ import print_function
from simpleconfigparser import simpleconfigparser

defaults = {
    'app': {
        'name': 'default'
    }
}

config = simpleconfigparser()
print(config.app.name)

config.read('read.ini')

print(config.app.debug)
print(config.app.getboolean('debug'))
print(config.app.verbose)
print(config.app.getboolean('verbose'))
print(config.app.name)
print(config.app.nope)
