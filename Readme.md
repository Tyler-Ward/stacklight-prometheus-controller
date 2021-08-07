Icinga status controller for the POE Stack Light 
================================================

This is a python script in a docker container which connects an Icinga network monitoring instance to a [POE stack light][blog-post].

The script is configured by the environment variables shown which set the location of the icinga instance and the stacklight.
The example docker-compose file give an template for configuring.

```
ICINGA_ADDRESS=localhost
ICINGA_PORT=5665
ICINGA_API_USER
ICINGA_API_PASSWORD
STACKLIGHT_ADDRESS
```

Information on the stacklight can be found in the following repositories.

* [Documentation][documentation-repo]
* [PCB designs][hardware-repo]
* [firmware][firmware-repo]


[blog-post]: https://www.scorpia.co.uk/2021/05/23/building-a-poe-enabled-lighting-fixture/
[documentation-repo]: https://github.com/Tyler-Ward/stacklight-documentation
[hardware-repo]: https://github.com/Tyler-Ward/stacklight-hardware
[firmware-repo]: https://github.com/Tyler-Ward/stacklight-firmware
