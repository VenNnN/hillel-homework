#!/usr/bin/env python3
import subprocess
from datetime import datetime
import datetime as DT
import random

subprocess.run('whoami')
subprocess.run('pwd')
subprocess.run('mkdir dz1', shell=True)
subprocess.run('cd dz1', shell=True)

command = 'touch '
current_datetime = datetime.now()
year = current_datetime.year
month = current_datetime.month
if month == 2:
    for i in range(1, 29):
        if i > 9:
            command += './dz1/' + str(i) + '-02-' + str(year) + '.log '
        else:
            command += './dz1/' + '0' + str(i) + '-02-' + str(year) + '.log '
else:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        for i in range(1, 32):
            if i > 9:
                command += './dz1/' + str(i) + '-' + str(month) + '-' + str(year) + '.log '
            else:
                command += './dz1/' + '0' + str(i) + '-' + str(month) + '-' + str(year) + '.log '
    else:
        for i in range(1, 31):
            if i > 9:
                command += './dz1/' + str(i) + '-' + str(month) + '-' + str(year) + '.log '
            else:
                command += './dz1/' + '0' + str(i) + '-' + str(month) + '-' + str(year) + '.log '

subprocess.run(command, shell=True)
subprocess.run('sudo chown -R root ./dz1/', shell=True)

if month == 2:
    randNum = random.sample(range(1, 29), 5)
else:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        randNum = random.sample(range(1, 32), 5)
    else:
        randNum = random.sample(range(1, 31), 5)

for num in randNum:
    command = 'rm ./dz1/'
    if num < 10:
        command += '0'
    command += str(num) + '-' + str(month) + '-' + str(year) + '.log'
    subprocess.run(command, shell=True)