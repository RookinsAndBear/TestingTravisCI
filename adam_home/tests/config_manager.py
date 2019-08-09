import json
import os

class Config(object):
    def __init__(self, config):
        self.config = config

    def get_environment(self):
        return self.config['env']

    def get_url(self):
        return self.config['url']

    def get_token(self):
        return self.config['token']

    def set_token(self, token):
        self.config['token'] = token

    def get_workspace(self):
        return self.config['workspace']

    def set_workspace(self, workspace):
        self.config['workspace'] = workspace


class ConfigManager(object):
    def __init__(self, file_name, raw_config=None):
        """ Initializes from the given file. If a file name is not given,
            checks raw_config, where it would expect a python dictionary
            as would be parsed using json from the config file.
        """

        if file_name is not None:
            print("filename = ", file_name)
            with open(file_name, 'r') as f:
                self.raw_config = json.load(f)
                print(self.raw_config)
                #print("env - workspace = ", self.raw_config['env_configs']['workspace'])
        elif raw_config is not None:
            self.raw_config = raw_config

        return self.raw_config

    def read_config(self, file_name):
        if file_name is not None:
            print("filename = ", file_name)
            with open(file_name, 'r') as f:
                self.raw_config = json.load(f)
                print(self.raw_config)
                #print("env - workspace = ", self.raw_config['env_configs']['workspace'])
        elif raw_config is not None:
            self.raw_config = raw_config

        return self.raw_config


    def get_config(self, environment=None):
        if environment is None:
            if 'default_env' in self.raw_config:
                environment = self.raw_config['default_env']

        if environment is None:
            print('Error: no environment given, and no default environement specified.')
            return None

        for config in self.raw_config['env_configs']:
            if config['env'] == environment:
                return Config(config)

        print("Error: could not find config for environment %s" % (environment))
        return self.raw_config['env_configs']['workspace']#None
        #return None

    def to_file(self, file_name):
        with open(file_name, 'w') as f:
            json.dump(self.raw_config, f, indent=4)

def main():
    output = ConfigManager(os.getcwd() + '\\TestingTravisCI\\test_config.json').get_config()
    print(output)

if __name__ == "__main__":
    main() 
