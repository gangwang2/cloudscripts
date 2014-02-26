#!/bin/bash 

#Public URL for Keystone API endpoint
AUTH_URL="http://16.173.247.240:5000/v2.0/tokens"
curl -i $AUTH_URL -X POST -H "Content-Type: application/json" \
      -H "Accept: application/json"  \
      -d '{"auth": { "tenantName": "AdminProject",
                       "passwordCredentials": 
                              { "username":"Admin", 
                                 "password":"secretword"
            } } }'
