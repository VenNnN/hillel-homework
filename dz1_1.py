#!/usr/bin/env python3
import subprocess
from datetime import datetime
import random
import calendar

subprocess.run('whoami')
subprocess.run('pwd')
subprocess.run('mkdir dz1', shell=True)
subprocess.run('cd dz1', shell=True)

command = 'touch '
for i in range(1, calendar.monthrange(datetime.now().year, datetime.now().month)[1] + 1):
    if i > 9:
        command += './dz1/' + str(i) + '-' + str(datetime.now().month) + '-' + str(datetime.now().year) + '.log '
    else:
        command += './dz1/' + '0' + str(i) + '-' + str(datetime.now().month) + '-' + str(datetime.now().year) + '.log '

subprocess.run(command, shell=True)
subprocess.run('sudo chown -R root ./dz1/', shell=True)

randNum = random.sample(range(1, calendar.monthrange(datetime.now().year, datetime.now().month)[1] + 1), 5)
print()
for num in randNum:
    command = 'rm ./dz1/'
    if num < 10:
        command += '0'
    command += str(num) + '-' + str(datetime.now().month) + '-' + str(datetime.now().year) + '.log'
    subprocess.run(command, shell=True)