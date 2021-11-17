import websocket, json
import pprint

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
  print('openned connection')

def on_close(ws):
  print('closed connection')

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


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()