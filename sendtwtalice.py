import twitter
import json
import time
import random

streams = []
with open('keys.tsv', 'r') as fKeysIn:
    for line in fKeysIn:
        line = line.rstrip().split('\t')
        streams.append(twitter.Api(consumer_key = line[0], consumer_secret = line[1], access_token_key = line[2], access_token_secret = line[3]))

random.seed(time.time())

charPerSec = 150 * 5 / 60 # spoken words per minute times 5

# create word list
words = list()
f = open('words', 'r')
for line in f:
    words.append(line)
    
# create word list from alice
alice = list()
f = open('aliceonesyl.txt', 'r')
for line in f:
    for word in line.split(' '):
        alice.append(word)

aliceidx = 0
while 1:
	# choose random account to post next item
    streamChoice = random.randint(0, len(streams) - 1)
    
    # build random line
    newline = "#AMNDBots " + str(aliceidx) + ' '
    while len(newline) < 140:
        if aliceidx >= len(alice):
            aliceidx = 0
        newword = alice[aliceidx]
        # print newword
        if len(newline + ' ' + newword) < 140:
            newline += ' ' + newword
            aliceidx += 1
        else:
            break
    print newline
    try:
        # pass
        streams[streamChoice].PostUpdate(newline)
    except Exception as e:
        print e
        print "Error.  Most likely duplicate post"
    stime = len(newline) / charPerSec
    time.sleep(stime)
				