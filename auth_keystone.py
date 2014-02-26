#!/usr/bin/python 
# OpenStack sdk
#
from string import Template
from os import environ as env
import keystoneclient.v2_0.client as ksclient
import novaclient.client as novaclient

keystone = ksclient.Client(auth_url=env['OS_AUTH_URL'],
                           username=env['OS_USERNAME'],
                           password=env['OS_PASSWORD'],
                           tenant_name=env['OS_TENANT_NAME'])
print "Token for Keystone:\n\n{0}".format(keystone.auth_token)

# Try to get service catalog
out_tpl = """
      domain name:${user_domain_name}, domain id:${user_domain_id}\n
      user id:${user_id}\n
      region name:${region_name}\n 
      tenant name:${tenant_name}, id:${tenant_id}
      """

tpl = Template(out_tpl)
kvs = {"user_domain_name": keystone.user_domain_name,
       "user_domain_id": keystone.user_domain_id,
       "user_id": keystone.user_id,
       "region_name": keystone.region_name,
       "tenant_name": keystone.tenant_name,
       "tenant_id": keystone.tenant_id
      }

result = tpl.substitute(kvs)

print result

compute_endpoint = keystone.service_catalog.url_for(
                     service_type="compute")
compute = novaclient.Client(compute_endpoint,
            token=keystone.auth_token)
print compute


       


