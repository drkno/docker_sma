import sys
import os
try:
    # python 2
    import ConfigParser as configparser
    import xmlrpclib
except:
    # python 3
    import configparser
    from xmlrpc import client as xmlrpclib

config = configparser.ConfigParser({
    'docker_host': 'http://localhost:7784/',
    'calling_from': 'manual',
    'remap_files_from': '/home/drkno/src/sickbeard_mp4_automator/t/files',
    'remap_files_to': '/files'
})
config.add_section('Call')

def remap_path(path_item):
    return path_item.replace(config.get('Call', 'remap_files_from'), config.get('Call', 'remap_files_to'))

if __name__ == '__main__':
    # load config
    if not os.path.exists('callConfig.ini'):
        with open('callConfig.ini', 'w') as configfile:
            config.write(configfile)
    config.read('callConfig.ini')

    environment_variable_prefixes = ('sonarr', 'radarr')

    env = {}
    for key in os.environ.keys():
        if any(key.lower().startswith(prefix) for prefix in environment_variable_prefixes):
            env[key] = remap_path(os.environ[key])

    argv = [remap_path(a) for a in sys.argv][1:]

    proxy = xmlrpclib.ServerProxy(config.get('Call', 'docker_host'))

    if config.get('Call', 'calling_from') == 'deluge':
        exit_code = proxy.deluge(env, argv)
    elif config.get('Call', 'calling_from') == 'sabnzbd':
        exit_code = proxy.sabnzbd(env, argv)
    elif config.get('Call', 'calling_from') == 'radarr':
        exit_code = proxy.radarr(env, argv)
    elif config.get('Call', 'calling_from') == 'sonarr':
        exit_code = proxy.sonarr(env, argv)
    elif config.get('Call', 'calling_from') == 'sickrage' or config.get('Call', 'calling_from') == 'sickbeard':
        exit_code = proxy.sickrage(env, argv)
    elif config.get('Call', 'calling_from') == 'nzbget':
        exit_code = proxy.nzbget(env, argv)
    elif config.get('Call', 'calling_from') == 'manual':
        exit_code = proxy.manual(env, argv)
    else:
        print('Invalid calling_from')

    exit(exit_code)
