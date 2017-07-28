from flask import Blueprint, Response, request
import json
import strip

_blueprint = Blueprint("API", __name__)
_blueprint_power = Blueprint("Power", __name__)
_blueprint_color = Blueprint("Color", __name__)
_blueprint_bright = Blueprint("Brightness", __name__)


def _response(status, body):
    return Response(response=json.dumps(body), mimetype="application/json", status=status)


def _get_body():
    return json.loads(request.data)


def _convert_to_rgb(color):
    blue = color % 256
    green = color / 256 % 256
    red = color / 256 / 256 % 256
    return red, green, blue


@_blueprint.route("/")
def _ping():
    return _response(200, {"pong": True})


@_blueprint_power.route("", methods=["GET"])
def _get_power():
    return _response(200, {"power": strip.get_status()})


@_blueprint_power.route("", methods=["POST"])
def _set_power():
    body = _get_body()
    strip.set_status(body["power"])
    return _response(200, {"power": strip.get_status()})


@_blueprint_color.route("", methods=["GET"])
def _get_color():
    red, green, blue = _convert_to_rgb(strip.get_color())
    return _response(200, {"red": red, "green": green, "blue": blue})


@_blueprint_color.route("", methods=["POST"])
def _set_color():
    body = _get_body()
    print(body)
    strip.set_color_rgb(body["red"], body["green"], body["blue"])
    red, green, blue = _convert_to_rgb(strip.get_color())
    return _response(200, {"red": red, "green": green, "blue": blue})


@_blueprint_bright.route("", methods=["GET"])
def _get_brightness():
    return _response(200, {"brightness": strip.get_brightness()})


@_blueprint_bright.route("", methods=["POST"])
def _set_brightness():
    body = _get_body()
    strip.set_brightness(body["brightness"])
    return _response(200, {"brightness": strip.get_brightness()})


def register(app):
    app.register_blueprint(_blueprint)
    app.register_blueprint(_blueprint_power, url_prefix="/power")
    app.register_blueprint(_blueprint_color, url_prefix="/color")
    app.register_blueprint(_blueprint_bright, url_prefix="/brightness")
