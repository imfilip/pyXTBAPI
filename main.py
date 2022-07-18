from websocket import create_connection
import json

with open("src/secrets.txt") as f:
    lines = f.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    print(f"USERNAME={username}, PASSWORD={password}")

# Problem polegał na tym, że należy korzystać z dwóch różnych adresów - jeden do logowania i zawierania transakcji: .../demo
# A drugi do pobierania m.in. stanu konta: .../demoStream
session = create_connection(f"wss://ws.xtb.com/demo")
data = {'command': 'login', 'arguments': {'userId': username, 'password': password}}
session.send(json.dumps(data))
response = json.loads(session.recv())

print("=====================")
print(response)
print("=====================")
print(response["streamSessionId"])

# Tworze drugie polaczenie.
stream_session = create_connection(f"wss://ws.xtb.com/demoStream")
print(stream_session)

print(stream_session.getstatus())

data = {"command": "getBalance", "streamSessionId": response["streamSessionId"]}
stream_session.send(json.dumps(data))
response = json.loads(stream_session.recv())


print(response)
print(response["data"]["balance"])