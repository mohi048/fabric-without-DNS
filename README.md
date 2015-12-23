# Fabric-without-DNS

DESCRIPTION
Fabric script to execute task based on ip address range when there is no DNS 
This is python script using fabric to configure instances on cloud such as openstack .
When you deploy a new instance and you do not have any DNS entry for new node , you 
can access it via ip address only. To configure multiple instances accessible only
via ip address range, use this script.
You can exclude the instances within the range of ip address
This script also check if SSH service is running.

USAGE
1. Install the python packages 
pip install -r requirements.txt

1.1 If PIP install fails , try
yum install fabric
apt-get install fabric


2. Update the config.ini with the instance credentials
   keep the config.ini file on the same directory where fab-new.py is located


3. Edit fab-new.py and update the variables

subnet_block -- Network range of your domain ie - 192.168.0

bl -- First IP in range

bu -- Last IP in range

excluded_hosts -- IP address to exclude from the fabric task

4. Define your custom tasks on the function "my_task" or you can create a new function

5. Execute the fabric task by passing the function name as argument to python file

fab -f fab-new.py my_task

