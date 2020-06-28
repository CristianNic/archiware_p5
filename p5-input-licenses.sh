#!/bin/sh

/usr/local/aw/bin/nsdchat -c License resources > /private/tmp/p5input-licenses.txt ; open /private/tmp/p5input-licenses.txt

/usr/local/aw/bin/nsdchat -c srvinfo hostid > /private/tmp/p5input-hostid.txt ; open /private/tmp/p5input-hostid.txt
/usr/local/aw/bin/nsdchat -c srvinfo port > /private/tmp/p5input-port.txt ; open /private/tmp/p5input-port.txt
/usr/local/aw/bin/nsdchat -c srvinfo platform > /private/tmp/p5input-platform.txt ; open /private/tmp/p5input-platform.txt
/usr/local/aw/bin/nsdchat -c srvinfo lexxvers > /private/tmp/p5input-lexxvers.txt ; open /private/tmp/p5input-lexxvers.txt
/usr/local/aw/bin/nsdchat -c srvinfo uptime > /private/tmp/p5input-uptime.txt ; open /private/tmp/p5input-uptime.txt

/usr/local/aw/bin/nsdchat -c srvinfo buildstamp > /private/tmp/p5input-buildstamp.txt ; open /private/tmp/p5input-buildstamp.txt
/usr/local/aw/bin/nsdchat -c srvinfo address > /private/tmp/p5input-address.txt ; open /private/tmp/p5input-address.txt
/usr/local/aw/bin/nsdchat -c srvinfo server > /private/tmp/p5input-server.txt ; open /private/tmp/p5input-server.txt
/usr/local/aw/bin/nsdchat -c srvinfo hostname > /private/tmp/p5input-hostname.txt ; open /private/tmp/p5input-hostname.txt
/usr/local/aw/bin/nsdchat -c srvinfo version > /private/tmp/p5input-version.txt ; open /private/tmp/p5input-version.txt
