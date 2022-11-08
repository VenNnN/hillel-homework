#!/usr/bin/env python3
import subprocess

subprocess.run('cp dz1_1.py dz1_run.py', shell=True)

subprocess.run('chmod u+x dz1_run.py', shell=True)

subprocess.run('chmod u=rx,g=,o= dz1_run.py', shell=True)

subprocess.run('python3 ./dz1_run.py', shell=True)