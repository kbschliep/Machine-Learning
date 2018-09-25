#!/usr/bin/env python
import json, sys, os
from urllib import urlopen
from urllib import urlencode
import urllib2
from time import sleep

SERVER="http://aflow.org"
API="/API/aflow-ml/v1.0"
MODEL="plmf"

poscar=open('POSCAR', 'r').read()
encoded_data = urlencode({'file': poscar,})

url = SERVER + API + "/" + MODEL + "/prediction"
request_task = urllib2.Request(url, encoded_data)
task = urllib2.urlopen(request_task).read()
task_json = json.loads(task)
results_endpoint = task_json["results_endpoint"]
results_url = SERVER + API + results_endpoint

incomplete = True
while incomplete:
    request_results = urllib2.Request(results_url)
    results = urllib2.urlopen(request_results).read()
    results_json = json.loads(results)
    if results_json["status"] == 'PENDING':
        sleep(10)
        continue
    elif results_json["status"] == 'STARTED':
        sleep(10)
        continue
    elif results_json["status"] == 'FAILURE':
        print("Error: prediction failure")
        incomplete = False
    elif results_json["status"] == 'SUCCESS':
        print("Successful prediction")
        print(results_json)
        incomplete = False
