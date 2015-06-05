#!/usr/bin/env python

import SoftLayer
import yaml


creds_file = open("softcreds.yaml",'r')
creds = yaml.load(creds_file)

client = SoftLayer.Client(username=(creds['username']), api_key=(creds['api_key']))

FH = open('kill-file','r')

kill_servers = FH.read().splitlines()

for server in kill_servers:
	print "Killing " + server
	client['Virtual_Guest'].deleteObject(id=server)

FH.close()
