import sys
import subprocess

#Consider rewriting this to create & use a virtual environment
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
