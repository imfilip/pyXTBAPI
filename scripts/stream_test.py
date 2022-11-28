from pkgutil import get_data
from websocket import create_connection
import json
import time
import websocket
import websockets
import _thread
import asyncio
from concurrent.futures import ThreadPoolExecutor

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
print(data_dict)
session_id = response["streamSessionId"]

print(session_id)


stream_session = create_connection(f"wss://ws.xtb.com/demoStream")
data_dict = {"command": "getCandles", "streamSessionId": session_id, "symbol": "BITCOIN"}
data = json.dumps(data_dict)


stream_session.send(data)
stream_session.send(json.dumps({"command": "getCandles", "streamSessionId": session_id, "symbol": "EURUSD"}))
stream_session.send(json.dumps({"command": "getKeepAlive", "streamSessionId": session_id}))

while True:
    result = stream_session.recv()
    # result = json.loads(result)
    print ("Received '%s'" % result)


# # _executor = ThreadPoolExecutor(1)

# # def sync_blocking():
# #     time.sleep(2)


# # async def hello_world():
# #     # run blocking function in another thread,
# #     # and wait for it's result:
# #     await loop.run_in_executor(_executor, sync_blocking)


# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(hello_world())
# # loop.close()

# # stream_session.send(data)
# # response = json.loads(stream_session.recv())
# # print(response)

# print("Jestem przed petla")

# # async def get_data():
# #     async with websockets.connect(f"wss://ws.xtb.com/demoStream") as websocket:
# #         print("przed wyslaniem")
# #         await websocket.send(data)
# #         print("Query has been sent!")
# #         response = await websocket.recv()
#         # # async for message in websocket:
#         # #    await process(message)
# #         print("Data has been received.")
# #         print("\n")
# #         print(response)

# # asyncio.get_event_loop().run_until_complete(get_data())


# async def get_data2():
#     uri = "wss://ws.xtb.com/demoStream"
#     async with websockets.connect(uri) as websocket:
#         await websocket.send(data)
#         while True:
#             try:
#                 print('Response:', await websocket.recv())
#             except websockets.ConnectionClosed:
#                 await websocket.send(data)
#                 print("Błąd, ale lecę dalej!")
#                 continue
# # Wydaje się, ze pomimo iz jest to websocket, to po stronie XTB nastepuje rozlaczenie jak chce ciagle odbierac dane:
# # HTTP load balancers or proxies that aren’t configured for long-lived connections may 
# # terminate connections after a short amount of time, usually 30 seconds, despite websockets’ keepalive mechanism.

# async def get_data3():
#     while True:
#         try:
#             await get_data2()
#         except:
#             print("Wysypałem się!")
#             continue

# asyncio.run(get_data2())


# # while True:
# #     response = json.loads(stream_session.recv())
# #     print(response)



# # # Define WebSocket callback functions
# # def ws_message(ws, message):
# #     print("WebSocket thread: %s" % message)

# # def ws_open(ws):
# #     ws.send('"command": "getCandles", "streamSessionId": {session_id}, "symbol": "BITCOIN"')

# # def ws_thread(*args):
# #     ws = websocket.WebSocketApp("wss://ws.xtb.com/demoStream", on_open = ws_open, on_message = ws_message)
# #     ws.run_forever()

# # # Start a new thread for the WebSocket interface
# # _thread.start_new_thread(ws_thread, ())

# # # Continue other (non WebSocket) tasks in the main thread
# # while True:
# #     time.sleep(5)
# #     print("Main thread: %d" % time.time())

# # # Rozwiazanie z tej strony: 
# # # https://support.kraken.com/hc/en-us/articles/360043283472-Python-WebSocket-recommended-Python-library-and-usage-examples



# # Patrz stronę:
# # https://websockets.readthedocs.io/en/3.4/intro.html
# # https://stackoverflow.com/questions/49822552/python-asyncio-typeerror-object-dict-cant-be-used-in-await-expression
# # https://stackoverflow.com/questions/33357233/when-to-use-and-when-not-to-use-python-3-5-await/33399896#33399896