===================================
git usage
===================================

global settings:
===================
- git config --global user.name "guohua"
- git config --global user.email "guohua@guohua.com"
- git config --global color.ui "always"


init:
===================
- git init
- git init --bare

.gitignore:
===================
files in this file will be ignored by all.

.git/info/exclude
===================
files in this file will be ignored by self, accept re.

add:
===================
- git add tmp.txt
- git add ``*``.txt
- git add .

commit:
===================
- git ci -m "add all" -a
- git ci -m "add tmp" tmp.txt
- git ci -C head -a --amend  # will not generate new commit record.

reset before commit:
=============================
- git co HEAD tmp.txt
- git co co HEAD \*.txt
- git co HEAD .

reset after commit:
========================
- git revert HEAD
- git revert commitID

- git reset HEAD

  #git status? no new file, so git add file, git commit

- git reset --soft HEAD/commitID

  #git status?  just commit is ok.

- git reset --hard HEAD/commitID

  #restore to the commitID completely.

branch:
===================
- git br
- git br -a
- git br newbr
- git co newbr
- git co -b newbr
- git br newbr bae470a1
- git br newbr1 newbr

clone:
===================
- git clone <url>

  will add 
	- remote.origin.url
	- remote.origin.fetch
	- branch.master.remote
	- branch.master.merge

- git remote add alias remoteURL
- git remote rm alias
- git push alias branch

fetch vs pull:
===================
- fetch: retrieve but not merge
- pull:	equals fetch and merge
	
rebase:
===================
	1. presume two br: test and master.
	2. both master and test have two new commits.
	3. we want to add the two new commits in test branch into master.
	4. git co master.
	5. git rebase test:
		a. it will checkout test as tmp branch.
		b. apply master patches(from test).
		c. resolve conflicts, add the file
		d. git rebase --continue.
		e. move to master branch, remove tmp branch.
	6. git rebase --abort     #give up rebase
	7. git rebase --skip	 #test branch will replace master.

merge:
===================
git merge commitID

  merge the patch in another branch with its commitID

push:
===================
- git push origin master

- create branch after clone:
        - git branch newbr
        - git push --set-upstream origin newbr

          it will create a new branch on remote server as well

alias:
===================
vi ~/.gitconfig
	
        - br = branch
        - st = status
        - co = checkout
        - ci = commit
        - ls=log --pretty=format:'%C(yellow)%h %C(blue)%ad%C(red)%d %C(reset)%s%C(green) [%cn]' --decorate --date=short
        - graph=log --graph --pretty=format':%C(yellow)%h%Cblue%d%Creset %s %C(white) %an, %ar%Creset'

check commit detail:
======================
- git show commitID

delete remote branch:
=======================
- git push origin :newfeature
- git branch -d newfeature

add SOB
