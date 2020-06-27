import os
import subprocess

def nsdchat_check():

    cmds = ['/usr/local/aw/bin/nsdchat -c License resources',
        '/usr/local/aw/bin/nsdchat -c srvinfo hostid',
        '/usr/local/aw/bin/nsdchat -c srvinfo version',
        '/usr/local/aw/bin/nsdchat -c srvinfo port',
        '/usr/local/aw/bin/nsdchat -c srvinfo hostname',
        '/usr/local/aw/bin/nsdchat -c srvinfo platform',
        '/usr/local/aw/bin/nsdchat -c srvinfo server',
        '/usr/local/aw/bin/nsdchat -c srvinfo lexxvers',
        '/usr/local/aw/bin/nsdchat -c srvinfo buildstamp',
        '/usr/local/aw/bin/nsdchat -c srvinfo address']

    output_file = open('temp.txt', 'wt')

    for cmd in cmds:
        proc = subprocess.Popen(cmd, shell=True, universal_newlines=True,
                            stdin=subprocess.PIPE,
                            stdout=output_file,
                            stderr=subprocess.PIPE)
        (output, err) = proc.communicate()
        print(output, end='')

    output_file.close()

def nsdchat_munkireport_formating():

    keys = ['license', 'hostid', 'version', 'port', 'hostname',
            'platform', 'server', 'lexxvers', 'buildstamp', 'address']
    values = []

    with open('temp.txt', 'rt') as f:
        for line in f:
            values.append(line.rstrip())

    dictionary = dict(zip(keys,values))
    f = open("output_nsdchat.txt","w")
    f.write("\n".join("{} = {}".format(k, v) for k, v in dictionary.items()))
    f.close()
    os.remove('temp.txt')

nsdchat_check()
nsdchat_munkireport_formating()

