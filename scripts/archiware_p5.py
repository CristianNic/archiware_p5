#!/usr/local/munki/python
# Archiware P5 script for MunkiReport

import os
import sys
import subprocess
import collections

def nsdchat_check():

    cmds = ['/usr/local/aw/bin/nsdchat -c License ArchivePlan free',
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

    out = []

    for cmd in cmds:
        proc = subprocess.Popen(cmd, text=True, shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        output, err = proc.communicate()
        out.append(output)

    values = [s.strip('\n') for s in out]
    values = [s.replace('-1', u'\u221E').rstrip() for s in out]

    keys = ['archive_plan', 'backup_plan', 'sync_plan', 'backup2go', 'client',
            'thin_client', 'virtual_client', 'device', 'jukebox', 'desktop_links',
            'host_id', 'port', 'platform', 'p5_version', 'uptime']

    dictionary = collections.OrderedDict(zip(keys,values))

    time = round(float(dictionary['uptime']), 1)
    day = time / (24 * 3600)
    time = time % (24 * 3600)
    hour = time / 3600
    time = time % 3600
    minutes = time / 60
    seconds = time

    dictionary['uptime'] = str("%dd %dh %dm" % (day, hour, minutes))

    return dictionary

def main():
    """Main"""
    # Check if Archiware P5 is installed
    if  not os.path.isfile('/usr/local/aw/bin/nsdchat'):
        print ("ERROR: Archiware P5 is not installed")
        exit(0)

    # Create cache dir if it does not exist
    cachedir = '%s/cache' % os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(cachedir):
        os.makedirs(cachedir)

    # Skip manual check
    if len(sys.argv) > 1:
        if sys.argv[1] == 'manualcheck':
            print ('Manual check: skipping')
            exit(0)

    # Get information about Archiware P5
    result = nsdchat_check()

    # Write results to cache
    os.chdir(cachedir)
    f = open("archiware_p5.txt","wt")
    f.write("\n".join("{} = {}".format(k, v) for k, v in result.items()))
    f.close()

if __name__ == "__main__":
    main()
