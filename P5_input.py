import subprocess
import os
import sys

subprocess.call(['df', '-h'])
print('---------')

subprocess.call(['ls', '-ls'])
print('---------')

cmd = ['ls', '-ls']
out = subprocess.Popen(cmd)
print(out)
print('---------')

cmd = ['/usr/local/aw/bin', './nsdchat -c License resources']
subprocess.Popen(cmd, stdout=file)
os.chdir('/private/tmp/')
file = open("output.txt", "w")
file.close()
