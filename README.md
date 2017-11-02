# Neomekit

💡 Server for Neopixels LEDs

## How to install it ?

First, clone this repo

````sh
$> git clone https://github.com/hug33k/Neomekit.git
````

Then install needed Python library ([Neopixel](https://github.com/jgarff/rpi_ws281x.git) & [Flask](http://flask.pocoo.org/))

````sh
$> ./install_neopixel.sh
$> pip install -r requirements.txt
````

And finally, you can launch Neomekit server

````sh
$> sudo python server.py
OR
$> sudo -E python server.py
````

( `-E` allows you to export your environment, needed because of `sudo` )

## How do I use it ?

You can use [homebridge-neomekit](https://github.com/hug33k/homebridge-neomekit.git) to controll your LEDs via Homekit (Apple).

Otherwise, you can use Neomekit API. ( Documentation available [here](DOCS.md) )

## FAQ

##### Why do I need to launch server in sudo mode ?

- Because `neopixel` library needs it.

##### Why do I need to use `-E` to use my environment ?

- Since we're using `sudo` to launch the server, we won't have access to __your__ environment but __root__'s environment.<br/>
If you want to use yours, you need to export it with `-E` flag.

##### How can I configure my LEDs ?

- You can check [here](DOCS.md) in ___Config___ section.<br/>
To add variable to your environment, you can do `export NEOMEKIT_key=value` ( It will only works for current session) or you can write previous command into you `.bashrc` ( If you're using `bash` ).

## TODO

- Daemon mode
- Logging
- Scenarios
