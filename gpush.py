#!/usr/bin/env python
import sys
import string

from user import *
from remote import *
from gerrit_version import *

if __name__ == "__main__":
	remote_name = check_remote(sys.argv[1])
	gerrit_ver = check_gerrit_version(sys.argv[1])

	if sys.argv[2].find('HEAD:refs/for/') == -1:
		branch_name = " HEAD:refs/for/"+sys.argv[2]
	else:
		branch_name = " "+sys.argv[2]

	num = print_ulist()
	sel_user = raw_input(">>>>Select reviewer (1~"+str(num)+") : ")
	sel_user = select_user(num, sel_user)

	reviewers=[]
	keys = DIC_USER.keys()
	for key in keys:
		if str(key) in sel_user:
			if gerrit_ver == "2.4.2":
				reviewers.append("--reviewer="+DIC_USER[key].split(':')[1])
			else:
				reviewers.append("r="+DIC_USER[key].split(':')[1])

	cmd_subset=""
	if len(reviewers):
		if gerrit_ver == "2.4.2":
			cmd_subset = "--receive-pack='git receive-pack "
			cmd_subset += " ".join(reviewers)
			cmd_subset += "' "
			target_cmd="git push "+cmd_subset+remote_name+branch_name
		else:
			cmd_subset = "%"
			cmd_subset += ",".join(reviewers)
			target_cmd="git push "+remote_name+branch_name+cmd_subset

	os.system(target_cmd)

