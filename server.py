import os
from flask import Flask
from api import register
from strip import setup
from misc import generate_color


def _get_var(name, default=None):
    try:
        return os.environ[name]
    except:
        return default

if __name__ == '__main__':
    app = Flask(__name__)
    setup({
        "count": int(_get_var("NEOMEKIT_LENGTH", 1)),
        "pin": int(_get_var("NEOMEKIT_PIN", 18)),
        "brightness":int( _get_var("NEOMEKIT_DEFAULT_BRIGHT", 100)),
        "color": generate_color(int(_get_var("NEOMEKIT_DEFAULT_COLOR", 16777215))),
        "freq": int(_get_var("NEOMEKIT_FREQ", 800000)),
        "dma": int(_get_var("NEOMEKIT_DMA", 5)),
        "invert": bool(_get_var("NEOMEKIT_INVERT", 0)),
        "channel": int(_get_var("NEOMEKIT_CHANNEL", 0)),
        "strip": int(_get_var("NEOMEKIT_STRIP", 1050624)),
    })
    register(app)
    app.run(port=int(_get_var("NEOMEKIT_PORT", 8080)), host="0.0.0.0")
