### Lame

## Services Running on Box

1. 21/tcp **ftp**
2. 22/tcp **SSH** (OpenSSH 4.7p1 Debian)
3. 139/tcp **Samba smbd 3.X - 3.X**
4. 445/tcp **Samba smbd 3.X - 3.X**
5. 3632/tcp **distccd v1** 

> So first I ran an nmap scan on the box. The scan was `nmap -A -T4 -p- <host_ip>`. This scans results can be seen in the file labeled "scan". After analyzing the scan I decided that although FTP anonymous login was allowed it probably would not get me anywhere. I made this decision because although there are known exploits for ftp they usually do not result in RCE. Next I began looking at the distccd service. This was interesting to see because I have never heard of this service before and it's concept is really cool! Naturally I spent a bit of time researching it out of curiosity and then began doing some exploit searching. I found an exploit in the exploitdb and loaded up metasploit. After setting my host and running the exploit I did end up with a low priv shell. WOOO! I played around and attempted to cd into root and was able to but when I tried to cat the flag I realized I had insufficient privileges. Rather than falling down a privilege escalating rabbit hole I decided to try exploiting the smb service. Unfortunately my nmap scan did not get an exact version of this service though. After searching through the exploit db and a lot of trial error I ended up guessing the version of smbd. I loaded up the exploit, set my rhost, and i popped a root shell! At this point I was able to cd into root and cat the flag!

## Some Things I Learned

> Although this box was very easy and I pretty much took the metasploit script kiddie route I definetely had a lot of fun doing it. I didn't really learn anything new in terms of offensive security but I did learn a lot about the distccd service. I really think this is a brilliant idea if implemented correctly
