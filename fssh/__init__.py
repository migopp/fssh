#!/usr/bin/python3

import subprocess

if __name__ == '__main__':
    subprocess.run(['chmod', '+x', 'fssh/init.sh'])
    subprocess.run(['./fssh/init.sh'])
