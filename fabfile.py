from fabric.api import *
from fabric.contrib.files import exists

# configuration for SSH
# env.user = ''
# env.hosts = []
# env.cwd = '/tmp'

def speak():
    local('say Hello World!')

def speak_custom(message):
    local('say %s' % message)


def hello():
    # write a message to a file on the server
    run('echo Hello GDI!! > gdi.txt')


def read_hello():
    # read the file from the server
    run('cat gdi.txt')


def hello_custom(message):
    # write a custom message to the server
    run('echo %s > gdi.txt' % message)


def delete_hello():
    # if the file exists, delete it
    if exists('gdi.txt'):
        run('rm gdi.txt')


def download_hello():
    get('gdi.txt')


def reset_hello():
    delete_hello()
    hello()
    read_hello()


def get_changed_files():
    cmd = 'git diff --name-only `git merge-base master HEAD`'
    # the `capture` parameter stores the stdout of the command in a variable
    changed_files = local(cmd, capture=True)
    return changed_files.split()


def jshint():
    changed_files = get_changed_files()
    changed_js = [f for f in changed_files if '.js' in f]
    # jshint the changed files
    cmd = 'jshint %s' % " ".join(changed_js)
    local(cmd)


def convert_mp3():
    # change to the music directory
    with lcd('music'):
        # get a list of files in the directory
        files = local('ls -1', capture=True).split()

        for in_file in files:
            out_file = in_file + '.mp3'
            # create a command like 'lame in.aif out.mp3'
            cmd = 'lame %s %s' % (in_file, out_file)
            local(cmd)


def delete_mp3():
    # change to the music directory
    with lcd('music'):
        files = local('ls -1', capture=True).split()
        for fname in files:
            if 'mp3' in fname:
                local('rm %s' % fname)



