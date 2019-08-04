import xmlrpclib
import subprocess
import os
from SimpleXMLRPCServer import SimpleXMLRPCServer
from shutil import copyfile

def call_common(script, env, args):
    e = os.environ.copy()
    e.update(env)
    return subprocess.call(["python", script] + args, env=e)

def deluge(env, args):
    return call_common("/app/base/delugePostProcess.py", env, args)

def sabnzbd(env, args):
    return call_common("/app/base/SABPostProcess.py", env, args)

def radarr(env, args):
    return call_common("/app/base/postRadarr.py", env, args)

def sonarr(env, args):
    return call_common("/app/base/postSonarr.py", env, args)

def sickrage(env, args):
    return call_common("/app/base/postConversion.py", env, args)

def nzbget(env, args):
    return call_common("/app/base/NZBGetPostProcess.py", env, args)

def manual(env, args):
    return call_common("/app/base/manual.py", env, args)

if __name__ == '__main__':
    # setup config file
    if not os.path.exists('/config/autoProcess.ini'):
        copyfile('/app/base/autoProcess.ini.sample', '/config/autoProcess.ini')
    if not os.path.exists('/app/base/autoProcess.ini'):
        os.symlink('/config/autoProcess.ini', '/app/base/autoProcess.ini')

    # start rpc server
    server = SimpleXMLRPCServer(("0.0.0.0", 7784))
    print "Listening on port 7784..."

    server.register_function(deluge, "deluge")
    server.register_function(sabnzbd, "sabnzbd")
    server.register_function(radarr, "radarr")
    server.register_function(sonarr, "sonarr")
    server.register_function(sickrage, "sickrage")
    server.register_function(nzbget, "nzbget")
    server.register_function(manual, "manual")

    server.serve_forever()
