# Neomekit

💡 Server for Neopixels LEDs

## How to install it ?

First, clone this repo

````sh
$> git clone https://github.com/hug33k/Neomekit.git
````

Then install needed Python library ([Neopixel](https://github.com/jgarff/rpi_ws281x.git) & [Flask](http://flask.pocoo.org/))

````sh
$> sh install_neopixel.sh
$> pip install -r requirements.txt
````

And finally, you can launch Neomekit server

````sh
$> sudo python server.py
````

## How do I use it ?

You can use [homebridge-neomekit](https://github.com/hug33k/homebridge-neomekit.git) to controll your LEDs via Homekit (Apple).

Otherwise, you can use Neomekit API.

## FAQ

#### Why do I need to launch server in sudo mode ?

Because `neopixel` library needs it.

## TODO

- API Doc
- Config support
- Daemon mode
- Logging
