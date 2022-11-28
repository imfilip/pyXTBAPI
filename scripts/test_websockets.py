import websockets
import asyncio
import json
from threading import Thread, Lock


with open("src/secrets.txt") as f:
    lines = f.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    print(f"USERNAME = {username}, PASSWORD = {password}")

# main_session = websockets.connect(f"wss://ws.xtb.com/demo")
data_dict = {"command": "login", "arguments": {"userId": username, "password": password}}
data = json.dumps(data_dict)


print("=================")
async def get_session():
    global x
    print("11111")
    async with websockets.connect(f"wss://ws.xtb.com/demo") as websocket:
        print("222222")
        await websocket.send(data)
        print("333333")
        response = json.loads(await websocket.recv())
        x = response["streamSessionId"]
        


asyncio.run(get_session())
print(x)
session_id = x


async def test():
    async with websockets.connect("wss://ws.xtb.com/demoStream") as websocket:
        await websocket.send({"command": "getCandles", "streamSessionId": x, "symbol": "BITCOIN"})
        response = await websocket.recv()
        print(response)
 
asyncio.get_event_loop().run_until_complete(test())