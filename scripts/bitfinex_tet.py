import json

from websocket import create_connection
ws = create_connection("wss://api-pub.bitfinex.com/ws/2")
#ws.connect("wss://api-pub.bitfinex.com/ws/2")
ws.send(json.dumps({
    "event": "subscribe",
    "channel": "book",
    "pair": "BTCUSD",
    "prec": "P0"
}))


while True:
    result = ws.recv()
    result = json.loads(result)
    print ("Received '%s'" % result)

ws.close()