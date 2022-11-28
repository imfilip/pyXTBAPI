import websocket
from websocket import create_connection
import ssl
import json


with open("src/secrets.txt") as f:
    lines = f.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    print(f"USERNAME = {username}, PASSWORD = {password}")

main_session = create_connection(f"wss://ws.xtb.com/demo")
data_dict = {"command": "login", "arguments": {"userId": username, "password": password}}
data = json.dumps(data_dict)
main_session.send(data)
response = json.loads(main_session.recv())

session_id = response["streamSessionId"]
print(session_id)

SOCKET = f'wss://ws.xtb.com/demoStream'

params = {
    "command": "getCandles", 
    "streamSessionId": session_id, 
    "symbol": "BITCOIN"}

def on_open(ws):
    print('Opened Connection')
    ws.send(json.dumps(params))

def on_close(ws):
    print('Closed Connection')

def on_message(ws, message):
    print (message)

def on_error(ws, err):
  print("Got a an error: ", err)


ws = websocket.WebSocketApp(SOCKET, on_open = on_open, on_close = on_close, on_message = on_message,on_error=on_error)
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})