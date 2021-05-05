#!/usr/bin/env python3

# Photon installer script

import os
import sys
from core.dependencies import haveDependencies, resolveDependencies


PHOTON_PATH = os.path.join(os.path.dirname(__file__), 'core', 'photon.py')

try:
    if sys.platform in {'linux', 'linux2', 'darwin'}:
        p_path = '/usr/local/bin/photon'
        try:
            os.remove(p_path)
        except FileNotFoundError:
            pass  # ensure the path does not exists
        os.symlink(PHOTON_PATH, p_path)
        os.chmod(PHOTON_PATH, 0o777)
    elif sys.platform in {'win32', 'cygwin', 'msys'} or os.name == "nt" or os.environ.get('OS', '') == 'Windows_NT':
        p_dir = os.path.expandvars('%ProgramFiles%\\Photon')
        if not os.path.exists(p_dir):
            os.mkdir(p_dir)
        with open(os.path.join(p_dir, 'photon.bat'), 'w') as w:
            w.write(f'@echo off\npython "{PHOTON_PATH}" %*')
        os.system(f'setx /M PATH "%PATH%;{p_dir}"')
    else:
        print('Automatic installation in this system is not supported yet.')
        input('Press enter to close')
        sys.exit(1)
except PermissionError:
    print('The installation failed due to lack of permissions.',
          'Run the proper script for your operational system or try to execute this as super user/administrator',
          sep='\n')
    input('Press enter to close')
    sys.exit(1)

if not haveDependencies('c', sys.platform):
    resolveDependencies('c', sys.platform)

print("Successfully installed! Now you can use the photon command!")
input('Press enter to close and play with Photon!')
