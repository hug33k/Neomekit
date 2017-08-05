# Neomekit Documentation

## Config

### Environment variables

| Variable | Type | Desc | Default |
|---|---|---|---|
| `NEOMEKIT_PORT` | Int | API port | 8080 |
| `NEOMEKIT_LENGTH` | Int | LED strip length | 1 |
| `NEOMEKIT_PIN` | Int | LED strip GPIO pin | 18 |
| `NEOMEKIT_DEFAULT_BRIGHT` | Int (From 0 to 255) | LED default brightness | 100 |
| `NEOMEKIT_DEFAULT_COLOR` | Int (Hex color as Int) | LED default color | 16777215 (#FFFFFF) |
| `NEOMEKIT_FREQ` | Int | LED display frequency | 800000 |
| `NEOMEKIT_DMA` | Int | LED DMA channel | 5 |
| `NEOMEKIT_INVERT` | Int (Bool as Int) | LED signal inversion | 0 (False) |
| `NEOMEKIT_CHANNEL` | Int | LED PWM channel | 0 |
| `NEOMEKIT_STRIP` | Int | LED strip type ( List available below ) | 1050624 ( WS2811_STRIP_RGB ) |

##### `NEOMEKIT_STRIP` types

- 4 color R, G, B and W ordering

| Code | Type |
|---|---|
| 403703808 | `SK6812_STRIP_RGBW` |
| 403701768 | `SK6812_STRIP_RBGW` |
| 403181568 | `SK6812_STRIP_GRBW` |
| 403177488 | `SK6812_STRIP_GBRW` |
| 402657288 | `SK6812_STRIP_BRGW` |
| 402655248 | `SK6812_STRIP_BGRW` |
| 4026531840 | `SK6812_SHIFT_WMASK` |

- 3 color R, G and B ordering

| Code | Type |
|---|---|
| 1050624 | `WS2811_STRIP_RGB` |
| 1048584 | `WS2811_STRIP_RBG` |
| 528384 | `WS2811_STRIP_GRB` |
| 524304 | `WS2811_STRIP_GBR` |
| 4104 | `WS2811_STRIP_BRG` |
| 2064 | `WS2811_STRIP_BGR` |

## API

###### GET /

Check if API is available

Response :
````json
{
  "status": true
}
````

### Power

###### GET /power

Get LED status

Response :
````json
{
  "power": true|false
}
````

###### POST /power

Set LED status

Body :
````json
{
  "power": true|false
}
````

Response :
````json
{
  "power": true|false
}
````

### Brightness

###### GET /brightness

Get LED brightness

Response :
````json
{
  "brightness": 0...255
}
````

###### POST /brightness

Set LED brightness

Body :
````json
{
  "brightness": 0...255
}
````

Response :
````json
{
  "brightness": 0...255
}
````

### Color

###### GET /color

Get LED color

Response :
````json
{
  "red": 0...255,
  "green": 0...255,
  "blue": 0...255
}
````

###### POST /color

Set LED color

Body :
````json
{
  "red": 0...255,
  "green": 0...255,
  "blue": 0...255
}
````

Response :
````json
{
  "red": 0...255,
  "green": 0...255,
  "blue": 0...255
}
````
