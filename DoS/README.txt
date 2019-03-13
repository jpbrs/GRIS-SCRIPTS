DoS and AntiDoS scripts

This directory contains 3 scripts:
1. dos.py
2. dos.sh
3. antidos.sh

Explaining the scripts

1. dos.py
This script is a malware created with the purpose of create the highest possible number of threads directed to send continous HTTP methods GET to a web server. This malware has the intuit of make a denial of service on a target host.

2. dos.sh
Like the first script, this one is just a shortcut to use slowhttptest with the same finality as the first one: Generate a DoS on a target web server.

3. antidos.sh
This script was created to block, using iptables,  any IP that tries to do a DoS attack. Remember that iptables is a command on bash that requires sudo privileges, so use sudo when execute this code.
<<<<<<< HEAD

PS: There are modules on Apache Web Server that can mitigates slow DoS attacks, but i wanted to create my own code as a challenge. By curiosity purpose, some famous modules are mod_reqtimeout, mod_qos and mod_security.
=======
>>>>>>> 5b98f2be3fd7e112dcb325b72f2bae32515a56a3
