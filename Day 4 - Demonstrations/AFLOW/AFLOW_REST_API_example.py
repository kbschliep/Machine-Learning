#!/usr/bin/env python
import json, sys, os
from urllib import urlopen

SERVER="http://aflowlib.duke.edu/AFLOWDATA"
PROJECT="/LIB3_RAW"
SET="/Cu_pvTi_svZn"
ENTRIES="/?aflowlib_entries"

response=urlopen( SERVER+PROJECT+SET+ENTRIES ).read()
response=response.rstrip()
print(response)
entry_list=response.split(",")
print(entry_list)                     
for i in xrange(len(entry_list)):
    entry=str(entry_list[i])
    URLentry_sg=SERVER+PROJECT+SET+"/"+entry+"/?spacegroup_relax"
    print(URLentry_sg)
    response=urlopen( URLentry_sg ).read()
    print(response)
