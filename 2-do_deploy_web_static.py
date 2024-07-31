#!/usr/bin/python3
"""A module for web application deployment with Fabric."""

import os
from fabric.api import env, put, run, sudo
from datetime import datetime

env.hosts = ['54.234.98.62', '54.88.200.151']
env.user = 'ubuntu'
env.key_filename = '/path/to/your/ssh/private/key'


def do_deploy(archive_path):
    """Deploy archive to web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]
        release_path = '/data/web_static/releases/{}'.format(archive_name)
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}/web_static/* {}'.format(release_path, release_path))
        run('rm -rf {}/web_static'.format(release_path))
        current_link = '/data/web_static/current'
        run('rm -rf {}'.format(current_link))
        run('ln -s {} {}'.format(release_path, current_link))
        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
