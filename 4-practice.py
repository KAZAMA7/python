#!/usr/bin/python3
spam = ['apples', 'bannanas', 'tofus', 'cats']

length = len(spam)

item = 0

while item < length - 1:
   print(spam[item], end=' ')
   item = item + 1

print(' and ' + spam[item])
