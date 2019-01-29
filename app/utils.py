import json
import os


def get_env_name():
    namespace = os.environ.get('ENVIRONMENT')
    return namespace.upper() if namespace else 'LOCAL'


def _load_config_file(name):
    with open(f'{name}.json') as f_obj:
        return json.load(f_obj)


def _update_dicts(dicts):
    super_dict = {}
    for d in dicts:
        if d is not None:
            super_dict.update(d)
    return super_dict


def get_config():
    config = _load_config_file('config')
    return _update_dicts([config['DEFAULT'], config.get(get_env_name()), os.environ])
