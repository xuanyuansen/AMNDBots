import twitter
import json
import time

streams = []
with open('keys.tsv', 'r') as fKeysIn:
    for line in fKeysIn:
        line = line.rstrip().split('\t')
        streams.append(twitter.Api(consumer_key = line[0], consumer_secret = line[1], access_token_key = line[2], access_token_secret = line[3]))

actorsEnum = ['THESEUS', 'HIPPOLYTA', 'EGEUS', 'LYSANDER', 'DEMETRIUS', 'PHILOSTRATE', 'QUINCE', 'SNUG', 'BOTTOM', 'FLUTE', 'STARVELING', 'HERMIA', 'HELENA', 'OBERON', 'TITANIA', 'PUCK', 'PEASBLOSSOM', 'COBWEB', 'MOTH', 'MUSTARDSEED', 'NARRATOR']

charPerSec = 150 * 5 / 60 # spoken words per minute times 5

itercount = 0
while 1:
	script = json.load(open('amnd.json'))
	count = 1
	itercount = itercount + 1
	for act in script['acts']:
		for scene in act['scenes']:
			for line in scene['lines']:
				if line['character'] in actorsEnum:
					print line['character']
					newline = str(itercount) + ':' + str(count) + ' ' + line['line']
					print newline
					try:
						streams[actorsEnum.index(line['character'])].PostUpdate(newline)
					except:
						print "Error.  Most likely duplicate post"
					stime = line['charcount'] / charPerSec
					count = count + 1
					time.sleep(stime)
				else:
					print line['character']
					print str(count) + line['line']
					newline = line['character'] + '\n' + str(itercount) + ':' + str(count) + ' ' + line['line']
					try:
						stream[len(actorsEnum) + 1].PostUpdate(newline)
					except:
						print "Error.  Most likely duplicate post."
					stime = line['charcount'] / charPerSec
					count = count + 1
					time.sleep(stime)