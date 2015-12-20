
#### Specify the first 3 block of ip range 
subnet_block = '192.168.0.'

#### Spcify the last block of ip range in block lower , block upper
bl = 99
bu = 119

###Specify the hosts you want to exclude , You can keep the list blank if there is no host to exclude on the range
excluded_hosts = ['192.168.0.117','192.168.0.118']
#excluded_hosts = []


import os
import socket;
import configparser
import time
import sys
from fabric.api import cd, env, prefix, run, task, execute
from fabric.colors import red, green, yellow
config = configparser.ConfigParser()
config.read('./config.ini')

vm_credentials = dict(config['SSH_CREDENTIALS'])
ssh_username = str(vm_credentials['ssh.username'])
ssh_password = str(vm_credentials['ssh.password'])

env.user = ssh_username
env.password = ssh_password
dead_host = []

def check_port(ips):
	print(green("Checking the SSH port"))
	time.sleep(3)
	for it in ips:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((it,22))
		if result==0:
		    pass
		else:
		    print(red("Server active but SSH not running on %s" %it))
		    env.hosts.remove(it)
		    dead_host.append(it)
	return env.hosts


def check_ip_active(subnet):
	print (green("Creating the subnet %s "%(subnet_block +"x")))
	print (green("Creating the IP range %s -- %s" %(subnet_block+str(bl) , subnet_block+str(bu)))) 
	time.sleep(3)
	if bl == 0 or bu >256:
		print ("Terminating the program !!!")
		sys.exit("Specify the correct ip range as defined in bl , bu")
	else:
		for i in range(bl,bu):
			hostname = subnet + str(i)
			env.hosts.append(hostname)
		for items in env.hosts:    
			response = os.system("ping -c 1 " + items )
			if response == 0:
				pass
			else:
				print (red("######  Could not ping %s !!! " %items))
				time.sleep(3)
				env.hosts.remove(items)
	return env.hosts



def exclude_hosts(hosts):
	for it in hosts:
		env.hosts.remove(it)
		print (yellow("Skipping host %s as user defined" %it))
		time.sleep(3)
	return env.hosts


check_ip_active(subnet_block)
if not excluded_hosts:
	pass
else:
	exclude_hosts(excluded_hosts)
check_port(env.hosts)
print "Total Active Hosts = ",len(env.hosts)
time.sleep(3)
print "Running jobs on host ",env.hosts
time.sleep(3)

###### define your fabric task over here
@task
def my_task():
	run('uptime')

