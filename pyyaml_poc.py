import yaml

stream = file('config.yml')
config = yaml.load(stream)
print config['foo']
print config['array']
