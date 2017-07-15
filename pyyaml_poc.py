import yaml

stream = file('config.yml')
config = yaml.safe_load(stream)
print config['foo']
print config['array']
