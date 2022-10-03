import sys
import subprocess

#try later -- re-write this as virtual environment
f = open('requirements.txt')
for line in f:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', line,])
f.close()
