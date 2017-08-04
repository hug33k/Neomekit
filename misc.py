import neopixel


def convert_to_rgb(color):
    blue = color % 256
    green = color / 256 % 256
    red = color / 256 / 256 % 256
    return red, green, blue


def generate_color(colors, color=None):
    if colors is None:
        return generate_color(convert_to_rgb(color))
    return neopixel.Color(colors[0], colors[1], colors[2])
