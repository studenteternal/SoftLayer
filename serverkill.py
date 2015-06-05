#!/usr/bin/python

import SoftLayer
import yaml

credsFile = open("softcreds.yaml",'r')
creds = yaml.load(credsFile)



client = SoftLayer.Client(username=(creds['username']), api_key=(creds['api_key']))

f = open('kill-file','r')

for line in f:
	
	s = f.readline()
	client['Virtual_Guest'].deleteObject(s)

close('kill-file')

