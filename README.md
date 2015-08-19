# AMNDBots
A collection of helper scripts and bots that act out the play "A Midsummer Night's Dream" on Twitter

keys.tsv follows the form: 
consumer_key|consumer_secret|access_token_key|access_token_secret
Where each key set is on its own line and | indices a tab.

shake.py - This script is a FSM designed to translate the Project Gutenberg version of William Shakespeare's A Midsummer Night's Dream into a json file that can be processed by the bot network. This script should work for similar documents with some modification.
Run with: python shake.py

sendtwtamnd.py - This script operates on the amnd.json file and coordinates the bot network to simulate the play at a speed similar to that of spoken word.
Run with: python sendtwtamnd.py

sendtwtalice.py - A simple script to iterate through text and post to a random bot network account.
Run with: python sendtwtalice.py