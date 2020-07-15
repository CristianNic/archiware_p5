#!/usr/local/munki/python
# Archiware P5 script for MunkiReport
# by Cristian Niculescu

import os
import sys
import subprocess
import collections
import plistlib
import json

def nsdchat_check():

    cmds = ['/usr/local/aw/bin/nsdchat -c srvinfo hostid',
            '/usr/local/aw/bin/nsdchat -c srvinfo port',
            '/usr/local/aw/bin/nsdchat -c srvinfo platform',
            '/usr/local/aw/bin/nsdchat -c srvinfo lexxvers',
            '/usr/local/aw/bin/nsdchat -c srvinfo uptime',
            '/usr/local/aw/bin/nsdchat -c License ArchivePlan free',
            '/usr/local/aw/bin/nsdchat -c License BackupPlan free',
            '/usr/local/aw/bin/nsdchat -c License SyncPlan free',
            '/usr/local/aw/bin/nsdchat -c License Backup2Go free',
            '/usr/local/aw/bin/nsdchat -c License Client free',
            '/usr/local/aw/bin/nsdchat -c License ThinClient free',
            '/usr/local/aw/bin/nsdchat -c License VirtClient free',
            '/usr/local/aw/bin/nsdchat -c License Device free',
            '/usr/local/aw/bin/nsdchat -c License Jukebox free',
            '/usr/local/aw/bin/nsdchat -c License DesktopLinks free']

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

    keys = ['host_id', 'port', 'platform', 'p5_version', 'uptime',
            'archive_plan', 'backup_plan', 'sync_plan', 'backup2go',
            'client', 'thin_client', 'virtual_client', 'device',
            'jukebox', 'desktop_links']

    dictionary = collections.OrderedDict(zip(keys,values))

    dictionary['port']   = int(dictionary['port'])
    dictionary['uptime'] = int(dictionary['uptime'])

    print(dictionary['uptime'])

    # format time
    import time
    dictionary['uptime'] = time.strftime('%d %H:%M:%S', time.gmtime(dictionary['uptime']))

    print(dictionary['uptime'])

    return dictionary

def main():
    """Main"""
    # Check if Archiware P5 is installed
    if  not os.path.isfile('/usr/local/aw/bin/nsdchat'):
        print ("ERROR: Archiware P5 is not installed")
        exit(0)

    # Get information about Archiware P5
    result = nsdchat_check()

    cachedir = '%s/cache' % os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(cachedir, 'archiware_p5.json'), 'w') as fp:
        json.dump(result, fp, indent=4)

if __name__ == "__main__":
    main()
