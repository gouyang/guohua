.. load-style:: big-centered

.. style:: 
    :align: center 
    :font_size: 48

**Linux basics**

**to make your life easy**

----

Installation

----

separating /home on your daily work PC

----

separating /var for web, databases

----

separating /boot for mutiple systems

----

.bashrc 

----

Export 

----

PATH="$HOME/bin:$PATH"

----

Alias

----

.bash_aliases

----

.. style:: 
    :align: left
    :font_size: 40

# Quick access

- alias ..='cd ..'
- alias ...='cd ../../../'
- alias dl='cd ~/Downloads/'
- alias doc='cd ~/Documents/'

----

# Systemctl

- alias status="systemctl status"
- alias start="systemctl start"
- alias stop="systemctl stop"
- alias restart="systemctl restart"

----

# Puppet

- alias docker="ssh 10.66.9.220 -l root"
- alias rhevh="ssh 10.66.11.225 -l root"

----

.. style:: 
    :align: center 
    :font_size: 48

git alias

----

.gitconfig for global

----

.git/config for local

----

Package Management

----

rpm

----

rpm -qc

----

rpm -qf

----

rpm -ql

----

rpm2cpio xxx.rpm | cpio -ivd

----

yum

----

yum repolist

----

yum clean all

----

yum provides

----

yum update -y

----

Language packages - Python,Nodejs,Go

----

pip install -U `yolk -U | awk '{print $1}' | uniq`

----

npm-check-updates -g

----

go get -u all

----

Text  manipulation

----

sed

----

sed -i 's/foo/bar/' filename

----

awk

----

awk -F":" '{print $NF}' /etc/passwd

----

File transition

----

rsync -avrztpg HostA:/dir HostB:/dir
