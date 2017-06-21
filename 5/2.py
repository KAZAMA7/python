#!/usr/bin/python3
### set default methods
import pprint

message = 'This is a bright morning with the sun rising in the east and moon wanning off it presence'

count = {}

for character in message:
   count.setdefault(character, 0)
   count[character] += 1
pprint.pprint(count)
