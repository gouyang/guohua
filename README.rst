Personal stuff
==============
Collect all my customize stuffs.

Window Manager
--------------

- awesome_

.. _awesome: https://github.com/awesomeWM/awesome

Editor
------

- vim

  plugins:

  * vundle_
  * nerdtree_
  * syntastic_
  * jedi_
  * supertab_

.. _vundle: https://github.com/gmarik/Vundle.vim.git
.. _nerdtree: https://github.com/scrooloose/nerdtree.git
.. _syntastic: https://github.com/scrooloose/syntastic
.. _jedi: https://github.com/davidhalter/jedi-vim
.. _supertab: https://github.com/ervandew/supertab


tools
-----

- hicat_

.. _hicat: https://github.com/rstacruz/hicat

- Presentation tools

  * hieroglyph_
  * rst2slides_
  * rst2s5_
  * pinpoint_

  .. _hieroglyph: https://github.com/nyergler/hieroglyph
  .. _rst2slides: https://bitbucket.org/tin_nqn/rst2slides
  .. _rst2s5: http://docutils.sourceforge.net/docs/user/slide-shows.html
  .. _pinpoint: https://github.com/GNOME/pinpoint

- github replacement

  * gitlab_
  * gitbucket_

  .. _gitlab: https://about.gitlab.com/
  .. _gitbucket: https://github.com/takezoe/gitbucket

git tips
--------

1. How to update forked repository?::

    git remote add upstream https://github.com/whoever/whatever.git
    git fetch upstream
    git checkout master
    git rebase upstream/master
    git push -f origin master

2. Save username/password for git::

    git config credential.helper store       
    git config credential.helper store 'cache --timeout=3600'

python tips
-----------

1. completion in interactive mode

   Add "export PYTHONSTARTUP=$HOME/.pythonrc.py" to $HOME/.bashrc

   Add below code into $HOME/.pythonrc.py::

      from jedi.utils import setup_readline
      setup_readline()

   .. Note:: Please install jedi firstly

nodejs
------

- bower_ package management

  .. _bower: https://github.com/bower/bower

codes
-----

1. download_ script to download files simultaneously

.. _download: /codes/download.py

slides collection
-----------------

- Python slides

  * `pycon 2013`_
    
.. _pycon 2013: https://speakerdeck.com/pyconslides/
