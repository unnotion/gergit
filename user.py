#!/usr/bin/env python
import os

DIC_USER = {
		1:'WK Kim:1@unknown.com',
		2:'JG Oh:2@unknown.com',
		3:'JC Jang:3@unknown.com',
		4:'HJ Park:4@unknown.com',
		5:'JO Song:5@unknown.com',
		6:'JH JI:6@unknown.com',
		7:'KN Kim:7@unknown.com',
		8:'SJ Choi:8@unknown.com',
		9:'SJ Lee:9@unknown.com',
		10:'WS Seon:10@unknown.com',
		11:'YS Lee:11@unknown.com'
		}

def print_ulist():
	print "+"+"-"*(2+3+10+30+4)+"+"
	for i in DIC_USER:
		token = DIC_USER[i].split(':')
		uname = token[0]
		mail = token[1]

		print "|",
		print str(i).rjust(3),
		print uname.ljust(10),
		print mail.ljust(30),
		print "|".rjust(3)
	print "+"+"-"*(2+3+10+30+4)+"+"

	return i

def select_user(num, param):
	# delete duplicate value
	token = list(set(param.replace(' ','').split(',')))

	i = 0
	for s in token:
		# check null string
		if s is '':
			del token[i]
		# check digit
		elif not s.isdigit():
			del token[i]
		# check range
		elif int(s) > int(num):
			del token[i]
		i+=1
	
	return token

