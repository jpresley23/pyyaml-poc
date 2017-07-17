import yaml

# Open file stream
stream = file('config.yml')

# safe load yaml file into variable
config = yaml.safe_load(stream)

# use
admin_server = config['admin-server']
print admin_server
