* What's list comprehension? can you give an example

  [x for x in xrange(10)]

* What's the difference between str() and repr()

  The str() function returns representations of values which are human-readable, while repr() generates representations which can be read by the interpreter.

* How to check code style for python code?

  pep8 and pylint

* Do you know virtual environment? What's the benefit to use it and how?

* sum 1..1000, write the code out there

  sum(xrange(1000))

* Do you know any difference between python 2 and python 3?

  * the print function changes
  * integer division changes (3 / 2 = 1 in python 2, 3 / 2 = 1.5 in python 3)
  * unicode redesign: python 3 has byte and bytearray 
  * xrange in python 3
  * exceptions: except NameError as err
  * ...

* Open a file and read it last 4K?

  could tell to use the seek method is fine. 

::

  with open("thefile") as fp:
      fp.seek(-4096, OS.SEEK_END)
      fp.read()
