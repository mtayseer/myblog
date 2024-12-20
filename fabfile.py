from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = '$ssh_user@$ssh_host:$ssh_port'
dest_path = '$ssh_target_dir'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = '$cloudfiles_username'
env.cloudfiles_api_key = '$cloudfiles_api_key'
env.cloudfiles_container = '$cloudfiles_container'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('echo y | rmdir /s {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    try:
        import pelicanconf
        if pelicanconf.THEME == 'theme/littlebigdetails':
            local('lessc theme/littlebigdetails/static/css/main.less > theme/littlebigdetails/static/css/main.css')
    except:
        pass
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    rebuild()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )


# Checkout presentations files
def checkout_submodules():
    with lcd(r'files\talks\\'):
        print 'Downloading Python4GCDC2013...'
        local('git clone https://github.com/mtayseer/Python4GCDC2013.git')
        print 'Downloading front-end-optimization...'
        local('git clone https://github.com/mtayseer/front-end-optimization.git')
