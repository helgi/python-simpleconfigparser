from __future__ import print_function
from simpleconfigparser import simpleconfigparser

config = simpleconfigparser()
config.read('read-dict-format.ini')

print(config.base.timeout)
print(config['www.example.com'].items())
print(config['www.example.com']['ssl'])
print(config['www.example.com'].getboolean('ssl'))
print(config['www.example.com']['timeout'])

print(config['www.example2.com']['timeout'])