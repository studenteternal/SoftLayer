#!/usr/bin/python

import yaml
import SoftLayer
from pprint import pprint 
import datetime
from datetime import datetime
from datetime import date

#filehandlers to load account specific information
credsFile = open("softcreds.yaml",'r')
creds = yaml.load(credsFile)

#print creds['username']
#print creds['api_key']

# variable declerations

load = {}
vservers = []
errorlist = {}
accountitems = []

client = SoftLayer.Client(username=(creds['username']), api_key=(creds['api_key']))

# this section loads the billing data for the current month
# -----------------------------------------------------------------------------------


filtermask = "mask[orderItem[order[userRecord[email]]]]"
getemailaddress = client['SoftLayer_Account'].getNextInvoiceTopLevelBillingItems(mask = filtermask)

# this section loads the active Virtual server list
# ------------------------------------------------------------------------------------



filtermask = "mask[hostname, id, provisionDate]"

nameandid1 = client['SoftLayer_Account'].getVirtualGuests(mask = filtermask)

#print type(nameandid1)
#print nameandid1[0]
vslength = len(nameandid1)

#print vslength
#print type(nameandid1)

# this loop associates the e-mail address and user to each virtual server for reporting.
# set loop counters
n = 0 
#t = vslength - 1
# seems to consistantly be missing the last virtual server when I compare results to verifiy so the -1 my be a mistake
t = vslength
m = 0
y = 0
cnt = 0
id = 0
error = 0
errorcount = 0
while (n < t):
	srv = nameandid1[n]	
	n = n + 1
	cnt = srv['id']
	m = 0
	while (y != cnt):
		try:
			x = getemailaddress[m]
#			print srv['id']
			y = x['resourceTableId']
			id = y
			m = m + 1
		except:
			errorlist[errorcount] = srv
			y = cnt
			print ("adding server to error file", srv)
			error = 1
			errorcount = errorcount + 1
	if (error == 0):
		a = x['orderItem']
		b = a['order']
		c = b['userRecord']
		d = c['email']
		srv['email'] = d
		vservers.append(srv)
		accountitems.append(srv)
	else:
		error = 0

#print vservers
#print "servers with errors"
#print errorlist
#	servers.append(load)  	

#print errorlist


# this section loads the active Physical server list
# ------------------------------------------------------------------------------------

filtermask = "mask[hostname, id, provisionDate]"

nameandid2 = client['SoftLayer_Account'].getHardware(mask = filtermask)
print 'this should be the baremetal servers'
print type(nameandid2)
print nameandid2

hwlength = len(nameandid2)

# list to associate e-mail address to bare metal server orders
# initialize loop variables 
n = 0 
t = hwlength
m = 0
y = 0
cnt = 0
id = 0
error = 0

while (n != t):
	srv = nameandid2[n]	
	n = n + 1
	cnt = srv['id']
	m = 0
	while (y != cnt):
		try:
			x = getemailaddress[m]
#			print srv['id']
			y = x['resourceTableId']
			id = y
			m = m + 1
		except:
			errorlist[errorcount] = srv
			print 'adding bare metal server to error list'
			y = cnt
			error = 1
			errorcount = errorcount + 1
	if (error == 0):
		a = x['orderItem']
		b = a['order']
		c = b['userRecord']
		d = c['email']
		srv['email'] = d
#		print (srv)
		accountitems.append(srv)
	else:
		error = 0

#print 'baremetal servers with errors'
#print errorlist
 
# this section load the active Neworking resources 
# ------------------------------------------------------------------------------------

# this section loads any other billing items on the account
# ------------------------------------------------------------------------------------

# This section simply appends all the item types into a master list of billing items
# ------------------------------------------------------------------------------------

#accountitems.append(vservers)

length = len(accountitems)
length = length 

#print length
#print 'this is the account list'
#print accountitems

# this section identifies hardware more then 7 days old and creates a new list of potential policy violations
# ------------------------------------------------------------------------------------

today = date.today()
#print today
#x = vservers[0]
#print x
#servertime = x['provisionDate']


#print servertime
#print type(servertime)
#servertime = servertime[:10]
#print servertime

#servertime = datetime.strptime(servertime, '%Y-%m-%d')
#servertime = datetime.date(servertime)
#print servertime

today = date.today()
#print today

#delta = today - servertime
#print delta.days

#intalize loop variables 
t = length 
n = 0
error == 0
while (n != t):
	try:
		item = accountitems[n]
		itemtime = item['provisionDate']
		itemtime = itemtime[:10]
		itemtime = datetime.strptime(itemtime, '%Y-%m-%d')
		itemtime = datetime.date(itemtime)
		delta = today - itemtime
#		print item
		if delta.days > 7:
			print item
#			wastetime = wastetime + 1
	except:
		errorlist[errorcount] = item
		y = n
		error = 1
		errorcount = errorcount + 1
	if (error == 0):
		n = n + 1
	else:
		error = 0
		n = n + 1

print 'server that had errors'
print errorlist

# this section removes any imortal items
# ---------------------------------------------------------------------------------------------



credsFile.close()

