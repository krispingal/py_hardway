#!/usr/bin/python

from sys import argv

script, cp1, cp2 = argv

fd1 = open(cp1)
fd2 = open(cp2, 'w')
fd2.write( fd1.read())
fd1.close()
fd2.close()
