#!/usr/bin/env python

import sys
from random import randrange

wordfile="/usr/share/dict/words"
if len(sys.argv)>1:
    if sys.argv[1]=="--help":
        print "Usage: %s [word-list]" % (sys.argv[0])
        print "Generates a list of four random words for a passphrase"
        print "Word-list defaults to /usr/share/dict/words"
        sys.exit(0)
    else:
        wordfile=sys.argv[1]

try:
    with open(wordfile) as f: pass
except IOError as e:
    print "Couldn't open %s for reading" % (wordfile)
    sys.exit(1)

words=[]
f=open(wordfile,'r')
for line in f:
    words.append(line)
indices=[randrange(len(words)) for i in range(4)]
passphrase=' '.join(words[j].strip() for j in indices)
print passphrase
