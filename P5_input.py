import subprocess
import os
import sys

subprocess.call(['df', '-h'])
print('---------')

subprocess.call(['ls', '-ls'])
print('---------')

cmd = ['ls', '-ls']
#output = subprocess.Popen(cmd, stdout=subprocess.PIPE)
out = subprocess.Popen(cmd)
print(out)
print('---------')

#output = proc.communicate()

# print(proc.returncode, output)

# from subprocess import Popen, PIPE
# proc = Popen(cmd, stdout=PIPE)



# os.chdir('/usr/local/aw/bin')

# cmd = ['location', 'command']
# cmd = ['cd /usr/local/aw/bin', 'sudo ./nsdchat -c License resources']
# output = subprocess.Popen(cmd, stdout=subprocess.PIPE)

#cmd = ['cd /usr/local/aw/bin', 'sudo ./nsdchat -c License resources']
#output = subprocess.Popen(cmd)
#print(output)
#print('---------')


cmd = ['/usr/local/aw/bin', './nsdchat -c License resources']
proc = subprocess.Popen(cmd, shell=False,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)

file = open("output.txt", "w")
subprocess.stdout.write(file)
file.close()

print(output)
print(err)
