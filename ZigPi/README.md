# ZigPi
ZigPi is a little Raspberry Pi Zero W used to run zigbe2mqtt (z2m).

## Zigbee2mqtt
Zigbee2mqtt has a good instruction page: <br>
But the Pi Zero has some issues as it does not support the latest nodeJS versions (or rather the other way round, Node does not support the old hardware)<br>
So there were some workarounds required:

### Node JS
I used these guides:
- https://github.com/nodejs/unofficial-builds/
- https://github.com/bnielsen1965/nodejs-install


### Python 3.6+
https://aruljohn.com/blog/python-raspberrypi/
this runs for a very,very long time on the little RPi Zero.<br>
I installed 3.11 (I think)


## Monitoring 
https://github.com/ironsheep/RPi-Reporter-MQTT2HA-Daemon/blob/master/RMTECTRL.md
