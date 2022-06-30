# SPIRIT
## Simple Python Instant Rangeban for IP Tables (SPIRIT) shell file generator

### Background
I initially created this script for my own personal use because I kept getting a lot of unwanted connections and brute force attempts on my network. Inputting CIDR IP Blocks one by one would have taken hours so instead I came up with a python script that takes a text file and turns it into a shell file complete with IP Table Drop packet commands. These text files with ip addresses can be found on some websites, as well as on other repositories on github. The shell file is then downloaded over ssh on the target machine and piped into bash. I'm sure there may be other solutions out there that are more elegant, but this is mine. 

### Usage Instructions
The script takes a text file that has ip addresses inside, separated by a newline. The ip.txt provided is an example file that you can use to see what happens. When the script first starts up, it will ask for a text file, complete with extension (so for the example file provided you would type in "ip.txt", or just copy the filename if your file system has extensions enabled). It is probably best to put this txt file in the same directory as the script. After which, it will process for a bit (might take a while for bigger files) and output a shell file with the commands + ips inside. This shell file will have a date attached in front in case you process multiple txt documents, avoiding a filename clash. <br>

That's about it. Use that shell file however you want. For me I piped it into bash so that the commands in the shell file execute. I verified it by using 
```
sudo iptables -S
```
Remember, IP Tables are reset on restart so look into persistence. 

### Processing Speed & Output Tests
So far, the "Instant" part is pretty true - 3515 IP addresses in CIDR notation (the entirety of china's IP address blocks, if I'm not mistaken) finishes instantly in pycharm and slightly under a second for IDLE. This same input file is about 52KB in size, or 52,000 characters. 

The output file is 164KB, or 164,000 characters. I have ideas on how to improve the file size but for now it seems marginal unless you're using it for super huge lists. 

### Additional Notes
There is little to no error checking for now, and I might update it some more - so please read the usage instructions before attempting anything. It takes a pretty specific file format.
