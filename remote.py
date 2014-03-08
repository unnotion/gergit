#!/usr/bin/env python
import sys
import subprocess

remote_list = subprocess.check_output(['git', 'remote']).split()

def select_remote():
	if 1 > len(remote_list):
		print ">>remote 0"
		sys.exit()
	if 1 == len(remote_list):
		remote_name = remote_list[0]
	else:
		num = 0
		print "-"*20
		for remote in remote_list:
			num+=1
			print str(num).ljust(3),
			print remote
		print "-"*20
		sel_remote = raw_input(">>>>Select remote (1~"+str(num)+") : ")
		remote_name = remote_list[int(sel_remote)-1]

	return remote_name


def check_remote(*arg_remote):
	if len(arg_remote) is 1:
		remote_name = arg_remote[0]
	else:
		remote_name =  select_remote()

	return str(remote_name)


def get_remote_full_addr(arg):
	remote_name = arg
	remote_list = subprocess.check_output(['git', 'remote', '-v']).split()

	i = 0
	limit = len(remote_list)
	dic_remote = {}
	while i < limit:
		dic_remote.update({remote_list[i]:remote_list[i+1]})
		i+=6

	for dic in dic_remote:
		if remote_name in dic_remote:
			remote_addr = dic_remote[remote_name]
			break

	return remote_addr

def get_remote_proto(arg):
	full_addr = get_remote_full_addr(arg)
	if full_addr.find("ssh://") != -1:
		proto = "ssh://"
	elif full_addr.find("http://") != -1:
		proto = "http://"
	elif full_addr.find("www.") != -1:
		proto = "http://"
	else:
		print ">> unknown protocol"
		sys.exit()

	return proto

def get_remote_addr(arg):
	full_addr = get_remote_full_addr(arg)
	proto = get_remote_proto(arg)

	return full_addr.split(proto)[1].split('/')[0]

def get_remote_repo(arg):
	full_addr = get_remote_full_addr(arg)
	proto = get_remote_proto(arg)
	addr = get_remote_addr(arg)

	return full_addr.replace(proto, '').replace(addr, '')
