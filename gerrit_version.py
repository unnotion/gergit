#!/usr/bin/env python
import sys
import subprocess

from remote import *

def check_gerrit_version(*param):
	if len(param) is 1:
		remote_name = param[0]
	else:
		remote_name =  select_remote()

	token = get_remote_addr(remote_name).split(':')

	port = '29418'
	#if len(token) == 2:
	#	port = token[1]
	#else:
	#	port = '29418'
	addr = token[0]

	ver = subprocess.check_output(['ssh', '-p', port, addr, 'gerrit', 'version']).split()

	return ver[2]

