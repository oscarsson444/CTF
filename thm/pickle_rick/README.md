# Picke Rick CTF TryHackMe

## 2023-12-31, Joakim Oscarsson

### Problem description
This Rick and Morty-themed challenge requires you to exploit a web server and find three ingredients to help Rick make his potion and transform himself back into a human from a pickle.

### Solution

### Nmap
nmap -sV -sC -p- -oN "output.txt" <Ip address>

Port 22 (ssh) and port 80 (HTTP) open

### Inspection:
Comment: Username=R1ckRul3s
robots.txt: Wubbalubbadubdub

### Gobuster
gobuster dir -w /usr/share/wordlists/dirb/common.txt -u 10.10.82.190

/.hta                 (Status: 403) [Size: 291]
/.htaccess            (Status: 403) [Size: 296]
/.htpasswd            (Status: 403) [Size: 296]
/assets               (Status: 301) [Size: 313] [--> http://10.10.82.190/assets/]
/index.html           (Status: 200) [Size: 1062]
/robots.txt           (Status: 200) [Size: 17]
/server-status        (Status: 403) [Size: 300]

### Dirbuster
Found few files and dirs like:
/login.php
/denied.php

Lead me to a cmd prompt containing the first ingredient

The next ingredient was hiding in the file system. Did a "ls -l" in / and found the home directory with a folder named "rick" there the second ingredient was hiding.

Next we run "sudo -l" to see what priviledges we have on the system and it turns out we can run sudo!

The third ingredient was hiding in the /root folder 


