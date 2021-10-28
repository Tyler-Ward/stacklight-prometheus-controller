#!/usr/bin/env python

import requests
import json
import time
import os

icinga_address = os.environ.get("ICINGA_ADDRESS","localhost")
icinga_port = os.environ.get("ICINGA_PORT","5665")
icinga_api_user = os.environ.get("ICINGA_API_USER")
icinga_api_password = os.environ.get("ICINGA_API_PASSWORD")
stacklight_address = os.environ.get("STACKLIGHT_ADDRESS")

if stacklight_address is None:
    print("STACKLIGHT_ADDRESS environment variable must be set")
    exit()

if icinga_api_user is None:
    print("ICINGA_API_USER environment variable must be set")
    exit()

if icinga_api_password is None:
    print("ICINGA_API_PASSWORD environment variable must be set")
    exit()

request_url = "https://{}:{}/v1/objects/services".format(icinga_address, icinga_port)
headers = {
        'Accept': 'application/json',
        'X-HTTP-Method-Override': 'GET'
        }
requestdata = {
        "attrs": [ "name", "state", "state_type", "last_hard_state", "acknowledgement"],
        "joins": [ "host.name", "host.state"],
}


while True:
    r = requests.post(request_url,
            headers=headers,
            auth=(icinga_api_user, icinga_api_password),
            data=json.dumps(requestdata),
            verify=False)

    maxstate=0;

    if (r.status_code == 200):
        data = r.json()
        print(data["results"])
        for service in data["results"]:
            if service["attrs"]["last_hard_state"]>maxstate and service["attrs"]["acknowledgement"] == 0:
                maxstate = service["attrs"]["state"]

        colour="off"
        if maxstate == 0:
            colour="off"
        elif maxstate == 1:
            colour="yellow"
        else:
            colour="red"

        print("setting to {}".format(colour))
        r = requests.post(
            "http://{}/set".format(stacklight_address),
            data="mode={}".format(colour),
            verify=False)

        time.sleep(5)
