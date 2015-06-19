#!/usr/bin/python

import yaml
import SoftLayer
from pprint import pprint 

credsFile = open("softcreds.yaml",'r')
creds = yaml.load(credsFile)

#print creds['username']
#print creds['api_key']

client = SoftLayer.Client(username=(creds['username']), api_key=(creds['api_key']))

n = 1
count = 1

kill_file = open("kill-file",'a')

while n < 5:
	server_name = 'jbsampsobuntutemp' + str(count) 
	n = n + 1
	server_return = client['Virtual_Guest'].createObject({
     		'datacenter': {'name': 'mex01'},
        	'hostname': server_name,
        	'domain': 'test.com',
        	'startCpus': 1,
        	'maxMemory': 4096,
        	'hourlyBillingFlag': 'true',
        	'localDiskFlag': 'false',
		'networkComponents': [{'maxSpeed': 1000}],
		'privateNetworkOnlyFlag': 'false',
		'blockDevices': [{'device': '0', 'diskImage': {'capacity': 100}}],
		'operatingSystemReferenceCode': 'UBUNTU_latest',
		'primaryBackendNetworkComponent': {'networkVlan': {'id': 773482}},
		'postInstallScriptUri': 'https://mex01.objectstorage.softlayer.net/v1/AUTH_3d7f3c03-9b34-418d-96f1-09a45712c21c/Jbsampso_startup_scripts/post_test.sh',
	})
	count = count + 1 
	kill_file.write(str(server_return['id']) + '\n')
#	print server_return
#	server_return = server_return.split(',')
#	print server_return[15]

kill_file.close()
credsFile.close()

#pprint( server_return )
#print server_return['id']
