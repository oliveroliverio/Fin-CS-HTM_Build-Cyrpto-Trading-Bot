# Fin-CS-HTM - Build a Crypto trading bot
[source](https://www.youtube.com/watch?v=GdlFhF6gjKo)

## 20211117 (replace with title at end of session)

### Requirements file

```
python-binance
TA-Lib
numpy
websocket_client
```

### Build bot.py base
Add methods

```python
import websocket

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m>"

def on_open():
  print('openned connection')

def on_close():
  print('closed connection')

def on_message():
  print('message received')

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
```

### Add parameters to functions

```python
import websocket

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m>"

def on_open(ws):
  print('openned connection')

def on_close(ws):
  print('closed connection')

def on_message(ws, message):
  print('message received')

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
```

test this by running bot.py

...Nothing's printing.

Trouble shoot by using `wscat`

```
wscat -c wss://stream.binance.com:9443/ws/ethusdt@kline_1m
```

output
```
< {"e":"kline","E":1637178604578,"s":"ETHUSDT","k":{"t":1637178600000,"T":1637178659999,"s":"ETHUSDT","i":"1m","f":676494419,"L":676494435,"o":"4226.28000000","c":"4226.35000000","h":"4226.42000000","l":"4226.28000000","v":"4.62330000","n":17,"x":false,"q":"19539.62436900","V":"2.47790000","Q":"10472.50553300","B":"0"}}
< {"e":"kline","E":1637178606880,"s":"ETHUSDT","k":{"t":1637178600000,"T":1637178659999,"s":"ETHUSDT","i":"1m","f":676494419,"L":676494527,"o":"4226.28000000","c":"4229.01000000","h":"4229.28000000","l":"4226.28000000","v":"80.72430000","n":109,"x":false,"q":"341285.92004500","V":"67.57180000","Q":"285669.66587200","B":"0"}}
```

it's working...

Bug fixed.  I had a `>` in SOCKET.

Print actual message

```python
def on_message(ws, message):
  print('message received')
  print(message)
```

convert message to JSON

```python
import json

def on_message(ws, message):
  print('message received')
  json_message = json.loads(message)
  print(json_message)
```

Pretty print json message
```python
import json
import pprint

def on_message(ws, message):
  print('message received')
  json_message = json.loads(message)
  pprint.pprint(json_message)
```

Note, looking at docs, 'k' is candle information.

Parse candle information:

```python
def on_message(ws, message):
  json_message = json.loads(message)
  candle = json_message['k']

  # parameter 'x' is boolean saying if candle is closed
  is_candle_closed = candle['x']
  # parameter 'c' is the value at closing
  close = candle['c']

  # print closing value if candle is closed
  if is_candle_closed:
    print("candle closed at {}".format(close))

```

stopped at 24:37