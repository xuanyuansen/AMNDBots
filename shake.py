from pprint import pprint
import json

f = open('amnd.txt', 'r')
out = open('amnd.json', 'w')

state = 0; # init
characters = list()
acts = list()
scenes = list()
lines = list()
scenecount = 0
actcount = 0

curchar = ""
curline = ""

# states
STATE_INIT = 0
STATE_CHAR_LIST = 1
STATE_ACT_PARSE = 2
STATE_NAR_PARSE = 3
STATE_BUILD_LINE = 4
STATE_END_LINE = 5

linenum = 0

for line in f:
	if line == 'Persons Represented.\n':
		print 'Found character list'
		state = STATE_CHAR_LIST # char list
	if state == STATE_CHAR_LIST:
		temp = line.split(':')
		if temp[0] == 'SCENE':
			print 'Found new scene: ' + temp[1].lstrip()
			state = STATE_ACT_PARSE # scene
		else:
			line = line.split(',')
			if len(line) == 2:
				print 'Found character: ' + line[0] + ' Description: ' + line[1].lstrip().split('.')[0]	
				characters.append({'name': line[0], 'description': line[1].lstrip().split('.')[0]})
			if len(line) == 3:
				print 'Found character: ' + line[0] + ' Description: ' + line[2].lstrip().split('.')[0]
				characters.append({'name': line[0], 'description': line[2].lstrip().split('.')[0]})
	if state == STATE_ACT_PARSE:
		if line.split(' ')[0] == 'ACT':
			if actcount > 0:
				scenes.append({'lines': lines, 'scene': scenecount})
				acts.append({'scenes': scenes, 'act': actcount});
			scenes = list()
			lines = list()
			actcount = actcount + 1
			scenecount = 0
			print 'Found act ' + str(actcount)
		elif line.split(' ')[0] == 'SCENE':
			if scenecount > 0:
				scenes.append({'lines': lines, 'scene': scenecount})
			scenecount = scenecount + 1
			print 'Found scene ' + str(scenecount)
			lines = list()
		elif line[0] == '[': # narrator
			print 'Found narrator line'
			line = line[1:-2]
			lines.append({'line': line, 'character': 'NARRATOR', 'charcount': len(line)})
			state = STATE_NAR_PARSE
		elif line.isupper():
			print 'Found line by ' + line.rstrip()
			curchar = line.rstrip()
			state = STATE_BUILD_LINE
			continue
	if state == STATE_NAR_PARSE:
		
		state = STATE_ACT_PARSE
	if state == STATE_BUILD_LINE:
		if line != '\n':
			if len(curline) + len(line.lstrip()) > 140:
				lines.append({'line': curline, 'character': curchar, 'charcount': len(curline)})
				curline = ""
			curline = curline + line.lstrip()
		else:
			state = STATE_END_LINE
	if state == STATE_END_LINE:
		lines.append({'line': curline, 'character': curchar, 'charcount': len(curline)})
		curline = ""
		state = STATE_ACT_PARSE

scenes.append({'lines': lines, 'scene': scenecount})
acts.append({'scenes': scenes, 'act': actcount});
output = {'acts': acts, 'characters': characters, 'play': "A Midsummer Night's Dream"}
json.dump(output,out)
	