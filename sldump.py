#!/usr/bin/python

import yaml
import SoftLayer
from pprint import pprint 

#ilehandlers to load account specific information
credsFile = open("softcreds.yaml",'r')
creds = yaml.load(credsFile)

#print creds['username']
#print creds['api_key']

# variable declerations
load = {}
servers = []


client = SoftLayer.Client(username=(creds['username']), api_key=(creds['api_key']))

n = 1
count = 1

# this line works, however there is an issue with the sub-filters not filtering.  
# preserving this line for education and refrence 
#filtermask = "mask[hostName, id, orderItem[order[userRecord[email]]]]"

filtermask = "mask[hostname, id]"

#nameandid1 = []

# this line is giving all the billing items for the month, including canceled devices
#  getemailaddress = client['SoftLayer_Account'].getNextInvoiceTopLevelBillingItems(mask = filtermask)
#print getemailaddress
n = 0 
y = ""

# thi is to test limiting the call with offest


#n = 0
#print type(getemailaddress)
#getemailaddress = {1}
#stop = {}
#while ( n < 1 ):
#	stop = getemailaddress
getemailaddress = client['SoftLayer_Account'].getNextInvoiceTopLevelBillingItems (mask = filtermask, id = 27950833)
print getemailaddress
#	print n
#	n = n + 1

# this works! 
#while (y != 'jbsampso-adnpub-bastion1'):
 #		x = {}
# 		x = getemailaddress[n]
# 		y = x['hostName']
# 		n = n + 1
# 	#	print x
# 		print x['orderItem']
# 		z = x['orderItem']
# 		print type(z)
# 		print  z['order']
# 		a = z['order']
# 		b = a['userRecord']
# 		print b
# 		c = a['userRecord']
# 		print c['email']
# 	
# 	#	print z['userRecord']
# 	
# 	#	print z['userRecord['email']']	


# Virtual servers - seperate sections will be needed for baremetal servers and other billing items. 

n = 0
m = 1
while (n < 6):
	nameandid1 = client['SoftLayer_Account'].getVirtualGuests(mask = filtermask, offset = 3)
		
	print nameandid1[n]
	print n
	n = n + 1
	m = m + 1
# print type(nameandid1)

#print nameandid1[0]

#temp = nameandid1[0]
#x = 0
#end = len(nameandid1)

#while (x < end): 
#	temp = nameandid1[x]
#	print temp['id']
#	temp2 = client['SoftLayer_Account'].getObject(temp['id'])
#	y = 0
#	z = 0
#	while (y != temp['id']):
#		onebillingitem = getemailaddress[z]
#		y = onebillingitem['id']
#		print y
#		print temp['id']
#		z = z + 1
#	print temp2
#	load = {'id' : temp['id'], 'hostname' : temp['hostname'], 'email' : temp2['email'], 'modifyDate' : temp2['modifyDate']}
#	print load
#	servers.append(load)  	
#	x = x + 1
		
#	print load

#print  client['SoftLayer_Account'].getObject(28668677)

#print servers


#print len(nameandid1)


#print client['SoftLayer_Account'].getObject('156844963')

credsFile.close()


#pprint( server_return )
#print server_return['id']
