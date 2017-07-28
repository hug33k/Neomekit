# Neomekit Documentation

## Config

TODO

## API

###### GET /

Check if API is available

Response :
````json
{
  "status": true
}
````

#### Power

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

#### Brightness

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

#### Color

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
