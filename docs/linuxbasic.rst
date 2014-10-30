.. load-style:: big-centered

.. style:: 
    :align: center 
    :font_size: 48

**Linux basics**

**to make the life easy**

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

- PATH="$HOME/bin:$PATH"
- PATH="$APPPATH/bin:$PATH"

----

Alias

----

.bash_aliases

----

.. style:: 
    :align: left
    :font_size: 40
# make sudo works as expect
alias sudo='sudo '

----

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

- alias mybox1="ssh 192.168.1.10 -l root"
- alias mybox2="ssh 192.168.1.20 -l root"

----

.. style:: 
    :align: center 
    :font_size: 48

git alias

----

- .gitconfig for global
- .git/config for local

----

.ssh/config 600

----

Host gitlab
    HostName gitlab.example.com
    Port 8080
    User root

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

RPM Fusion

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

assumeyes=1  /etc/yum.conf

----

Language packages - Python,Nodejs,Go

----

pip install -U `yolk -U | awk '{print $1}' | uniq`

----

- npm update -g single-pkg
- npm-check-updates -g

----

- go get -u single-pkg
- go get -u all

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
