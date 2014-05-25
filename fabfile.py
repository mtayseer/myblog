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
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('lessc theme/littlebigdetails/static/css/main.less > theme/littlebigdetails/static/css/main.css')
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

def watch_n_serve():
    from bottle import route, run, static_file
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    OUTPUT_ROOT = './output'

    @route('/')
    @route('/<path:path>')
    def serve(path='index.html'):
        response = static_file(path, root=OUTPUT_ROOT)

        # if the user wants a directory, I search for index pages
        if path.endswith('/') and response.status_code == 404:
            for file in ['index.html', 'index.htm']:
                response = static_file(path + file, root=OUTPUT_ROOT)
                if response.status_code != 404:
                    return response
        return response

    class BuildEventHandler(FileSystemEventHandler):
        def on_moved(self, event):
            super(BuildEventHandler, self).on_moved(event)
            rebuild()

        on_created = on_deleted = on_modified = on_moved

    event_handler = BuildEventHandler()
    observer = Observer()
    observer.schedule(event_handler, './content', recursive=True)
    observer.start()
    try:
        run(host='localhost', port=8080, debug=True)
    finally:
        observer.stop()
        observer.join()

# Checkout presentations files
def checkout_submodules():
    with lcd(r'files\talks\\'):
        print 'Downloading Python4GCDC2013...'
        local('git clone https://github.com/mtayseer/Python4GCDC2013.git')
        print 'Downloading front-end-optimization...'
        local('git clone https://github.com/mtayseer/front-end-optimization.git')
