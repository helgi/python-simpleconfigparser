from simpleconfigparser import simpleconfigparser

config = simpleconfigparser()
config.app.name = 'Magic App'
config.settings.limit = 10000
config.write('write.ini')
