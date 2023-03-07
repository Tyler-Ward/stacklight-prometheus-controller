#!/usr/bin/env python

import requests
import json
import time
import os


prometheus_address = os.environ.get("PROMETHEUS_ADDRESS","localhost")
prometheus_port = os.environ.get("PROMETHEUS_PORT","9090")
prometheus_query = os.environ.get("PROMETHEUS_QUERY")
threshold_yellow = int(os.environ.get("THRESHOLD_YELLOW",50))
threshold_yellow_down = int(os.environ.get("THRESHOLD_YELLOW_DOWN",threshold_yellow))
threshold_red = int(os.environ.get("THRESHOLD_RED",75))
threshold_red_down = int(os.environ.get("THRESHOLD_RED_DOWN",threshold_red))
stacklight_address = os.environ.get("STACKLIGHT_ADDRESS")

if prometheus_query is None:
    print("PROMETHEUS_QUERY environment variable must be set")
    exit()

request_url = "http://{}:{}/api/v1/query?query={}".format(
        prometheus_address, prometheus_port,
        requests.utils.quote(prometheus_query, safe=""))
headers = {
        'Accept': 'application/json',
        'X-HTTP-Method-Override': 'GET'
        }

colour = "off"

while True:
    r = requests.get(request_url,
            headers=headers,
            verify=False)

    if (r.status_code == 200):
        data = r.json()
        # print(data);
        value = int(data["data"]["result"][0]["value"][1])
        # print(value)

        if colour == "off":
            if value >= threshold_yellow:
                colour_next="yellow"
            if value >= threshold_red:
                colour_next="red"
        elif colour == "yellow":
            if value < threshold_yellow_down:
                colour_next="off"
            if value >= threshold_red:
                colour_next="red"
        elif colour == "red":
            if value < threshold_red_down:
                colour_next="yellow"
            if value < threshold_yellow_down:
                colour_next="off"
        else:
            colour = "off"
            colour_next = "off"
            
        if colour_next != colour:
            colour=colour_next
            print("setting to {}".format(colour))

        try:
            r = requests.post(
                "http://{}/set".format(stacklight_address),
                data="mode={}".format(colour),
                verify=False)
        except requests.exceptions.ConnectionError:
            print("Unable to Connect to stacklight")


    time.sleep(5)
