#! /usr/bin/env python3
# bulletPointAdder.py - Adds Wikipedia markup bullets to the beginning of each list item


import pyperclip

text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)