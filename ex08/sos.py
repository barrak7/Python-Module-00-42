#!/bin/python

import sys


def checker(s):
	for i in s:
		if ((i.isalpha() == False) and (i.isdigit() == False) and (i != ' ')):
			return (0)
	return (1)

n = len(sys.argv)

if (n < 2):
	sys.exit()

i = 1
while i < n:
	if (sys.argv[i].isalnum() == False):
		if (checker(sys.argv[i]) == 0):
			print("ERROR")
			sys.exit()
	i = i + 1

a = {'A':'.- ', 'B':'-... ', 'C':'-.-. ', 'D':'-.. ', 'E':'. ',
				'F':'..-. ', 'G':'--. ', 'H':'.... ',
				'I':'.. ', 'J':'.--- ', 'K':'-.- ',
				'L':'.-.. ', 'M':'-- ', 'N':'-. ',
				'O':'--- ', 'P':'.--. ', 'Q':'--.- ',
				'R':'.-. ', 'S':'... ', 'T':'- ',
				'U':'..- ', 'V':'...- ', 'W':'.-- ',
				'X':'-..- ', 'Y':'-.-- ', 'Z':'--.. ',
				'a':'.- ', 'b':'-... ', 'c':'-.-. ',
				'd':'-.. ', 'e':'. ',
				'f':'..-. ', 'g':'--. ', 'h':'.... ',
				'i':'.. ', 'j':'.--- ', 'k':'-.- ',
				'l':'.-.. ', 'm':'-- ', 'n':'-. ',
				'o':'--- ', 'p':'.--. ', 'q':'--.- ',
				'r':'.-. ', 's':'... ', 't':'- ',
				'u':'..- ', 'v':'...- ', 'w':'.-- ',
				'x':'-..- ', 'y':'-.-- ', 'z':'--.. ',
				'1':'.---- ', '2':'..--- ', '3':'...-- ',
				'4':'....- ', '5':'..... ', '6':'-.... ',
				'7':'--... ', '8':'---.. ', '9':'----. ',
				'0':'----- ',' ':'/ '}

i = 1
while i < n:
	if i < n - 1:
		for c in sys.argv[i]:
			print(a[c], end="")
		print(a[' '], end='')
	else:
		for c in sys.argv[i]:
			print(a[c], end="")
		print('')
	i = i + 1
