#!/usr/bin/python3
"""let python   all Web static files"""
from fabric.api import local
from time import strftime


def do_pack():
    """let the func  from contents of web_static"""

    name = strftime('%Y%m%d%H%M%S')
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static".format(name))
        return ("versions/web_static_{}.tgz".format(name))
    except Exception:
        return None
