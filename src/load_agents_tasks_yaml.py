import yaml


# defining file paths for YAML configurations
files = {
    'agents' : 'config/agents.yaml',
    'tasks' : 'config/tasks.yaml',
}

# laoding configurations from yaml files
config ={}

for key, file_path in files.items():
    with open(file_path, 'r')as file:
        config[key] = yaml.safe_load(file)

# assign loaded configurations to specifc variables

agents_config = config['agents']
tasks_config = config['tasks']