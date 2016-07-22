#!/bin/bash

sudo dnf update -y
sudo dnf install -y gcc awesome git ansible vim-enhanced vpnc thunderbird Zim stardict stardict-dic-zh_CN pidgin

sudo pip install --upgrade pip
sudo pip install vim-power

mkdir -p $HOME/git $HOME/.config/awesome $HOME/.vim

git clone https://github.com/gouyang/wm-awesome $HOME/.config/awesome
git clone https://github.com/gouyang/guohua $HOME/git/guohua

sudo cp HOME/git/guohua/repos/* /etc/yum.repos/
sudo dnf install -y google-chrome-stable 

cp ~/guohua/custom/bashrc ~/.bashrc
cp ~/guohua/custom/bash_alias ~/.bash_alias

git clone https://github.com/gouyang/vim $HOME/.vim/
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
vim -c "PluginInstall" -c "qa"

# set up for go
git clone https://github.com/golang/go $HOME/go1.4
cp -r go1.4 go1.7

# Automatic Login
#[daemon]
#AutomaticLogin=username
#AutomaticLoginEnable=True

# dnf 
# assumeyes=True  /etc/dnf/dnf.conf
# proxy=https://squid.xxx.com  /etc/yum.repos/

# NOPASSWD sudo
# /etc/sudoers

# locale
# modify /etc/locale.conf

# fedy to install skype etc
curl http://folkswithhats.org/fedy-installer
dnf install ibus-qt.i686  # chinese IM support

# vim go plugins

go get -u github.com/nsf/gocode
go get -u github.com/alecthomas/gometalinter
go get -u golang.org/x/tools/cmd/goimports
go get -u golang.org/x/tools/cmd/guru
go get -u golang.org/x/tools/cmd/gorename
go get -u github.com/golang/lint/golint
go get -u github.com/rogpeppe/godef
go get -u github.com/kisielk/errcheck
go get -u github.com/jstemmer/gotags
go get -u github.com/klauspost/asmfmt/cmd/asmfmt
go get -u github.com/fatih/motion
go get -u github.com/zmb3/gogetdoc
go get -u github.com/josharian/impl

# gitconfig
git config --global push.default simple
git config --global user.name "Guohua Ouyang"
git config --global user.email "ouyanggh0815@gmail.com"
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.st status
git config --global core.editor vim
git config --global credential.helper store

