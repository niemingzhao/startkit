#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import getopt
import getpass
import os
import shutil
import sys
import venv


def is_in_virtual_environment():
    return (bool(os.environ.get('VIRTUAL_ENV')) or
            hasattr(sys, 'real_prefix') or
            getattr(sys, 'base_prefix', sys.prefix) != sys.prefix)


def exit_with_help():
    print(r"""
Usage: startkit [--help] [--dst PATH] <PROJECT_NAME>

Options:
  -h, --help            show this help message and exit
  --dst PATH            destination path where the project will be created

e.g.
  startkit --dst C:\workspace myproject
    """)
    sys.exit()


def main():
    if is_in_virtual_environment():
        print('Error: Cannot run in virtual environment.')
        sys.exit()
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help', 'dst='])
    except Exception as err:
        print('Error: %s' % err)
        sys.exit()
    dest = ''
    project = ''
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            exit_with_help()
        elif opt == '--dst':
            dest = arg
        else:
            exit_with_help()
    if len(args):
        project = args[0]

    if not dest:
        dest = os.getcwd()
        __ = '> Where will the project be created? [%s] ' % dest
        dest = input(__).strip() or dest
    if not os.path.exists(dest) or not os.path.isdir(dest):
        try:
            os.makedirs(dest)
        except Exception as err:
            print('Error: %s' % err)
            sys.exit()
    dest = os.path.abspath(dest)
    if not project:
        project = 'myproject'
        __ = '> Please enter your project name: [%s] ' % project
        project = input(__).strip() or project
    dest = os.path.join(dest, project)
    package = project.replace('-', '_')
    __ = '> Please enter main package name: [%s] ' % package
    package = input(__).strip() or package
    version = '0.0.1'
    __ = '> Please enter your project version: [%s] ' % version
    version = input(__).strip() or version
    description = 'None.'
    __ = '> Please enter your project description: '
    description = input(__).strip() or description
    author = getpass.getuser()
    __ = '> Please enter your name: [%s] ' % author
    author = input(__).strip() or author
    email = 'Unknown'
    __ = '> Please enter your email: '
    email = input(__).strip() or email
    date = str(datetime.datetime.now().year)

    table = {
        '{{ project }}': project,
        '{{ package }}': package,
        '{{ version }}': version,
        '{{ description }}': description,
        '{{ author }}': author,
        '{{ email }}': email,
        '{{ date }}': date
    }

    try:
        shutil.copytree(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'templates'), dest)
    except Exception as err:
        print('Error: %s' % err)
        sys.exit()
    for root, dirs, files in os.walk(dest):
        for name in dirs:
            path = os.path.join(root, name)
            base = os.path.basename(path)
            for key, value in table.items():
                base = base.replace(key, value)
            if path != os.path.join(root, base):
                os.rename(path, os.path.join(root, base))
        for name in files:
            file = os.path.join(root, name)
            base = os.path.basename(file)
            for key, value in table.items():
                base = base.replace(key, value)
            if file != os.path.join(root, base):
                os.rename(file, os.path.join(root, base))
    for root, dirs, files in os.walk(dest):
        for name in dirs:
            pass
        for name in files:
            file = os.path.join(root, name)
            with open(file, 'r', encoding='utf-8') as f:
                try:
                    lines = f.readlines()
                except:
                    continue
            with open(file, 'w', encoding='utf-8') as f:
                for line in lines:
                    for key, value in table.items():
                        line = line.replace(key, value)
                    f.write(line)
    venv.create(os.path.join(dest, 'venv'), with_pip=True)

    print(r"""
The project has been created successfully!

To get started:

  cd %s
  venv\Scripts\activate.bat (cmd.exe)
  venv\Scripts\Activate.ps1 (PowerShell)
  source venv/bin/activate (bash/zsh)
  pip install -r requirements.txt
  pip freeze > requirements.txt
  python -m %s
  ...
  deactivate

Documentation can be found at https://pypi.org/project/startkit.
    """ % (dest, package))


if __name__ == '__main__':
    main()
