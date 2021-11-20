import websocket, json
import pprint

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

# these will eventually be variable
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'BTCUSD'
TRADE_QUANTITY = 0.05
closes = []

def on_open(ws):
  print('openned connection')

def on_close(ws):
  print('closed connection')

def on_message(ws, message):
  global closes
  json_message = json.loads(message)
  candle = json_message['k']

  is_candle_closed = candle['x']
  close = candle['c']

  if is_candle_closed:
    print("candle closed at {}".format(close))
    closes.append(float(close))
    print("closes")
    print(close)

    if len(closes) > RSI_PERIOD:
      np_closes = np.array(closes)
      rsi = talib.RSI(np_closes, RSI_PERIOD)
      print("all RSIs calc'd so far")
      print(rsi)
      last_rsi = rsi[-1]
      print("the current rsi is {}".format(last_rsi))

      if last_rsi > RSI_OVERBOUGHT:
        print("go buy")

      if last_rsi < RSI_OVERSOLD:
        print("go sell")


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()