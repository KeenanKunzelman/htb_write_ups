# Devel

## Services Running on Box

1. 21/tcp **ftp** (anonymous login allowed)
2. 80/tcp **http** (Microsoft IIS httpd 7.5)

## Initial enumeration
> First I checked out the website running on the machine by typing 10.10.10.5 into my browser and I got to the default IIS webpage. After confirming that there is actually something running on the machine I decided to check out what I could do with ftp. After logging in anonymously and noticing that I was in the websites root directory I decided to enumerate this service. 

## Exploiting ftp

> Since I am trying to do all of these boxes without using metasploit to prepare for oscp I decided to try and generate some shell code myself. I used **msfvenom** to do this. At first I thought this would be as easy as grabbing the first windows reverse shell and using ftp to transfer it onto the server. This would have been fine if I was using a metasploit listener to catch the shell but since I planned on using net cat I needed to learn about staged and unstaged payloads. After reading this awsome [article](https://medium.com/@hakluke/haklukes-guide-to-hacking-without-metasploit-1bbbe3d14f90) I realized I needed to use an unstaged payload. I went with the `windows/shell_reverse_tcp`. I generated a `.aspx` file and uploaded it to the server with ftp. I then spun up a listener using `nc -nvlp 4444` and told the webserver to run my file.

## Low-priv Shell

> I'm in! Well sort of... My I did catch the shell but it is low-priv. Next I tried to run PowerUp.ps1 a privesc powershell script but I had no luck. The user account my shell was running under was not allowed to run any scripts. So after a minor defeat I ran systeminfo to get an idea of the system I was on and to feed this to windows-exploit-suggester. This is something I should have done the second I got a shell but you win some and you lose some. After running this I noticed that the machine had quite a few Kernel vulns that would lead to privesc. I chose to use **ms11-046.exe**.

## Privesc

> Now this is the part I wasted the most time over silly issues. I fell down a giant rabbit hole here becasue I when I uploaded the exploit to the server. I never changed the upload mode to binary which lead to me getting a message that read `this program can not be executed in DOS mode`. After trying about 5 different exploits and wasting a bunch of time I did a bit more research and decided to try and re-upload but in binary mode. BINGO after this I ran the exploit and rooted the box!


