from src.api import SessionXTB

with open("src/secrets.txt") as f:
    lines = f.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    print(f"USERNAME={username}, PASSWORD={password}")

connection_XTB = SessionXTB(main_address = f"wss://ws.xtb.com/demo", stream_address = f"wss://ws.xtb.com/demoStream")

print(connection_XTB)
connection_XTB.login(username, password)
print(connection_XTB.session_id)

print(connection_XTB.getBalance())
connection_XTB.logout()
