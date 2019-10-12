#!/usr/bin/python3/
# bulletadder.py - an automatic bullet adder to the clipboard 
import pyperclip 
# message = 'list of apple\n list of banana\n list of aloo\n list of nothing\n well i don\'t know ?'

m = pyperclip.paste()
msg = m.split("\n")
new_msg = list()
print(msg)
for i in msg :
    new_msg.append("* "+ i.strip())
pyperclip.copy(('\n'.join(new_msg)))
