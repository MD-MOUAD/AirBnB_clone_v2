#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py)
 that creates and distributes an archive to your web servers,
 using the function deploy:
"""

from datetime import datetime
from os.path import isdir, exists
from fabric.api import put, run, env, local

env.hosts = ['3.94.185.86', '35.153.50.176']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    file_name = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%-m%-d%-H%-M%-S")
    )

    if isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        dest_path = f"/data/web_static/releases/{no_ext}"
        if (
            put(archive_path, '/tmp/').failed or
            run(f'mkdir -p {dest_path}/').failed or
            run(f'tar -xzf /tmp/{file_name} -C {dest_path}/').failed or
            run(f'rm /tmp/{file_name}').failed or
            run(f'mv {dest_path}/web_static/* {dest_path}/').failed or
            run(f'rm -rf {dest_path}/web_static').failed or
            run(f'rm -rf /data/web_static/current').failed or
            run(f'ln -s {dest_path}/ /data/web_static/current').failed
        ):
            return False
    except Exception:
        return False
    print("New version deployed!")
    return True


def deploy():
    """
    Create and distribute an archive to a web server
    """
    file_name = do_pack()
    if file_name is None:
        return False
    return do_deploy(file_name)
