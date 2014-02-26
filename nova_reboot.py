#!/usr/bin/python 
# OpenStack sdk
#
from string import Template
from os import environ as env
import novaclient.client as novaclient

nova_version = "2"
compute = novaclient.Client(nova_version, 
                            username=env['OS_USERNAME'],
                            api_key=env['OS_PASSWORD'],
                            project_id=env['OS_TENANT_NAME'],
                            auth_url=env['OS_AUTH_URL'])

#Get servers
server_mgr = compute.servers
server_list = server_mgr.list(limit=10)

for server in server_list:
  print 'Server {0} is in state {1}'.format(server.name, server.status)
  if server.status == 'ACTIVE' :
     # read input
     opt=raw_input("Do you want to reboot this server?(y/n)[y]:")
     if opt != 'n' :
         opt = raw_input( "Please choose Reboot Type. s=Soft, h=Hard [s]:")
         reboot_type='SOFT'
         if opt == 'h':
	     reboot_type = 'HARD' 
         opt=raw_input("please confirm. (y/n)[n]:")
         if opt == 'y':
             server.reboot(reboot_type)
             print 'reboot action performed'
         else:
             print ' pass.'
     else:
         print 'pass.' 

  else:
     print 'Non-active server is not eligible to reboot'


