#!/bin/sh
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig
cd /tmp
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install
