#!/bin/bash -x

#Public URL for Keystone API endpoint
AUTH_URL="http://127.0.0.1:5000/v2.0/tokens"
curl -i $AUTH_URL -X POST -H "Content-Type: application/json" \
      -H "Accept: application/json"  \
      -d '{"auth": { "tenantName": "service",
                       "passwordCredentials": 
                              { "username":"nova", 
                                 "password":"password"
            } } }'
