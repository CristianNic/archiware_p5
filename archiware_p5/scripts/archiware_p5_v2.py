#!/usr/bin/python
# Archiware P5 script for MunkiReport
# by MatX Macvfx and CristianNic for MunkiReport

import os
import subprocess
import collections

def nsdchat_check():

    cmds = ['/usr/local/aw/bin/nsdchat -c License resources',
        '/usr/local/aw/bin/nsdchat -c License ArchivePlan free',
        '/usr/local/aw/bin/nsdchat -c License BackupPlan free',
        '/usr/local/aw/bin/nsdchat -c License SyncPlan free',
        '/usr/local/aw/bin/nsdchat -c License Backup2Go free',
        '/usr/local/aw/bin/nsdchat -c License Client free',
        '/usr/local/aw/bin/nsdchat -c License ThinClient free',
        '/usr/local/aw/bin/nsdchat -c License VirtClient free',
        '/usr/local/aw/bin/nsdchat -c License Device free',
        '/usr/local/aw/bin/nsdchat -c License Jukebox free',
        '/usr/local/aw/bin/nsdchat -c License DesktopLinks free',
        '/usr/local/aw/bin/nsdchat -c srvinfo hostid',
        '/usr/local/aw/bin/nsdchat -c srvinfo port',
        '/usr/local/aw/bin/nsdchat -c srvinfo platform',
        '/usr/local/aw/bin/nsdchat -c srvinfo lexxvers',
        '/usr/local/aw/bin/nsdchat -c srvinfo uptime',]

    output_file = open('temp.txt', 'wt')

    for cmd in cmds:
        proc = subprocess.Popen(cmd, shell=True, universal_newlines=True,
                            stdin=subprocess.PIPE,
                            stdout=output_file,
                            stderr=subprocess.PIPE)
        (output, err) = proc.communicate()
        print(output)

    output_file.close()

def nsdchat_munkireport_formating():

    keys = ['license resources', 'ArchivePlan', 'BackupPlan', 'SyncPlan',
            'Backup2Go', 'Client', 'ThinClient', 'VirtClient', 'Device',
            'Jukebox', 'DesktopLinks', 'hostid', 'port', 'platform',
            'lexxvers', 'uptime']
    values = []

    with open('temp.txt', 'rt') as f:
        for line in f:
            values.append(line.rstrip())

    dictionary = collections.OrderedDict(zip(keys,values))
    dictionary['uptime'] = str(round((float(dictionary['uptime'])/3600), 1))+" hours"

    f = open("archiware_p5.txt","w")
    f.write("\n".join("{} = {}".format(k, v) for k, v in dictionary.items()))
    f.close()
    os.remove('temp.txt')

def main():
    """Main"""
    # Check if Archiware P5 is installed
    if  not os.path.isfile('/usr/local/aw/bin/nsdchat'):
        print "ERROR: Archiware P5 is not installed"
        exit(0)

    # Get information about Archiware P5
    nsdchat_check()

    # Write results to cache
    nsdchat_munkireport_formating()

if __name__ == "__main__":
    main()
