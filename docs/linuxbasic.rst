.. load-style:: big-centered

**Linux basics**

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

make your life easy

----

Export 

----

PATH="$HOME/bin:$PATH"

----

Alias

----

.bash_aliases

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

- alias docker="ssh 10.66.9.220 -l root"
- alias rhevh="ssh 10.66.11.225 -l root"

----

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

Language packages - Python,nodejs

----

pip install -U `yolk -U | awk '{print $1}' | uniq`

----

npm-check-updates -g

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
