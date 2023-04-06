#!/usr/bin/python3
"""fabric script to create and archive for the webstatic"""

from fabric.api import local
from datetime import datetime
from fabric.decorators import run_once


@runs_once
def do_pack():
    """ generate a .tgz folder"""
    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    result = local("tar -czvf versions/{} web_static".format(archive_name))

    if result.failed:
        return None

    return "versions/{}".format(archive_name)
