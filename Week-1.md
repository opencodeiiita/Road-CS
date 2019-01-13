# Week-1 : Lab Setup and Basics

**( Timeline : 12<sup>th</sup> January'19 - 19<sup>th</sup> January'19 )**
1. Partitioning of Pendrive
2. Linux Installation (Preferably Ubuntu)
3. Proxy setting up using different environment variables , like 
	* all_proxy
	* http_proxy
	* https_proxy
	* Setting in **/etc/environment** file etc
4. Linux Basic Commands (eg. ls, cd, grep, chmod)
5. Bascis of SSH and SSH tunnelling,  SCP , SFTP ( how to connect to digital ocean/aws or any other VPSes )
6.Shell scripting , Automating as many tasks as possible.
7.Set up **2 VMs** ,
	1. Vagrant [EpicTreasure](https://github.com/ctfhacker/EpicTreasure) and change according to your needs ( like it has 8gb RAM and 4 cores assigned for the virtual box , change it accordingly to suit your system ).
	2. The 2nd being [Flare-VM](https://github.com/fireeye/flare-vm) windows virtual machine.

These two would contain moslty all the tools you would ever need for either Windows reversing or Linux reversing/pwning or basic maleware analysis.


|#| Task		| Points	|	Format To Submit	|
|--| ------------- 	| -------------	|	-------------------		|
|1| Partitioning of pendrive<sup>a</sup>  | 30  |	S	|
|2| Setting up of Linux OS<sup>b</sup> | 30  |		S	|
|3| Proxy Setting using export command  | 10  |		C	
|4| Proxy Setting by adding in .bashrc file  | 20  |	S	|
|5| SSH tunnelling ( one liner script )<sup>d</sup>  | 10  |	C	|
|6| One liner to copy a _folder_ to a directory named **week-1** on remote server/vagrant VM  | 30  |	C	|
|7| SFTP connection to the remote server/ vagrant VM  | 30  |	S	|
|8| Setting up vagrant VM  | 50  |		G/V	|
|9| Setting up vagrant Flare-VM  | 50  |		G/V	|
|10| **BONUS** : Master Question<sup>c</sup>	| 50	|	S	|
|| **TOTAL** 	| **310**	|

a) Create two partition of pendrive of equal size and submit screenshots.

b) Either make live USB in one of the partition of pendrive or Set it up in virtual box(or vmware).

c) Show the output of `lsof` to show the port is opened and which program is running on this port.

**Sample Output ( I have tunnelled on port 8123 )**
![Sample output of lsof -i:8123](https://user-images.githubusercontent.com/17861054/39735433-2e224300-5299-11e8-87c9-101f0979a36b.png)

d) Coming soon..


Index	|	|
--------|-------|
C	| Code	|
S	| Screenshot	|
G/V	| Gif/Video	|


### enjoy hacking :)
### try harder
