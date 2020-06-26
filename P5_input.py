import subprocess
import os
import sys

out = subprocess.call(['df', '-h'])
print(out)
print('---------')

cmd = ['ls', '-ls']
out2 = subprocess.Popen(cmd)
print(out2)
print('---------')

cmd = ['/usr/local/aw/bin', './nsdchat -c License resources']
subprocess.Popen(cmd, stdout=file)
os.chdir('/private/tmp/')
file = open("output.txt", "w")
file.close()
