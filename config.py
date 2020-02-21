import yaml

# Load YAML file and create global config object.
f = open("config.yaml")
config = yaml.load(f, Loader=yaml.SafeLoader)
f.close()
