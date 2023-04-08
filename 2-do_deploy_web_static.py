#!/usr/bin/python3

"""script to fully deploy python program"""

import os
from fabric.api import env, put, run

env.hosts = ['54.160.100.61', '100.25.152.160']

def do_deploy(archive_path):
    """
    deploy webstatic to servers
    Args:
        archive_path - the path to the archive
    Returns:
        true if all operations are a succesc else false
    """

    if not os.path.exists(archive_path):
        return False
    archive_filename = os.path.basename(archive_path)
    archive_foldername = archive_filename.replace(".tgz", "")
    path = "/data/web_static/releases/{}/".format(archive_foldername)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(archive_filename))
        run("mkdir -P {}".format(archive_foldername))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, path))
        run("rm -rf /tmp/{}".format(archive_filename))
        run("mv {}web_static/* {}".format(path, path))
        run("rm -rf {}web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
