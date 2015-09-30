# fabric-without-DNS
Fabric script to execute task based on ip address range when there is no DNS 
This is python script using fabric to configure instances on cloud such as openstack .
When you deploy a new instance and you do not have any DNS entry for new node , you 
can access it via ip address only. To configure multiple instances accessible only
via ip address range, use this script.
You can exclude the instances within the range of ip address
This script also check if SSH service is running or not/.
