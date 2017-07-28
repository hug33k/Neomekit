import neopixel

_default_conf = {
    "count": 140,
    "pin": 18,
    "freq": 800000,
    "dma": 5,
    "brightness": 100,
    "invert": False,
    "channel": 0,
    "strip": neopixel.ws.WS2811_STRIP_GRB,
    "color": neopixel.Color(255, 255, 255)
}
_status = True
_brightness = None
_color = None
strip = None


def _merge_conf(conf, defaults):
    result = defaults
    for item in conf:
        result[item] = conf[item]
    return result


def setup(conf):
    global strip
    conf = _merge_conf(conf, _default_conf)
    strip = neopixel.Adafruit_NeoPixel(conf["count"], conf["pin"], conf["freq"], conf["dma"], conf["invert"], conf["brightness"], conf["channel"], conf["strip"])
    strip.begin()
    set_brightness(conf["brightness"])
    set_color(conf["color"])


def set_brightness(value, save=True):
    global strip, _brightness
    if save:
        _brightness = value
    strip.setBrightness(value)
    strip.show()


def get_brightness():
    return _brightness


def set_color(value):
    global strip, _color
    _color = value
    for index in range(strip.numPixels()):
        strip.setPixelColor(index, _color)
    strip.show()


def set_color_rgb(red, green, blue):
    global strip, _color
    _color = neopixel.Color(red, green, blue)
    for index in range(strip.numPixels()):
        strip.setPixelColor(index, _color)
    strip.show()


def get_color():
    return _color


def get_status():
    return _status


def set_status(value):
    global _status
    _status = value
    if value:
        set_brightness(_brightness)
        set_color(_color)
    else:
        set_brightness(0, False)