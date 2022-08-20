Prometheus query controller for the POE Stack Light 
================================================

This is a python script in a docker container which connects an prometheus metrics collection system to a [POE stack light][blog-post].
It is derived from the [script][stacklight-icinga-controller] used to display icinga results on the stacklight.

The script is configured by the environment variables shown which set the location of the prometheus instance and the stacklight.
The example docker-compose file give an template for configuring.

```
PROMETHEUS_ADDRESS=localhost
PROMETHEUS_PORT=9090
PROMETHEUS_QUERY
THRESHOLD_YELLOW=50
THRESHOLD_RED=75
STACKLIGHT_ADDRESS
```

Information on the stacklight can be found in the following repositories.

* [Documentation][documentation-repo]
* [PCB designs][hardware-repo]
* [firmware][firmware-repo]


[blog-post]: https://www.scorpia.co.uk/2021/05/23/building-a-poe-enabled-lighting-fixture/
[stacklight-icinga-controller]:https://github.com/Tyler-Ward/stacklight-icinga-controller
[documentation-repo]: https://github.com/Tyler-Ward/stacklight-documentation
[hardware-repo]: https://github.com/Tyler-Ward/stacklight-hardware
[firmware-repo]: https://github.com/Tyler-Ward/stacklight-firmware
