from src.api import SessionXTB

with open("src/secrets.txt") as f:
    lines = f.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    print(f"USERNAME = {username}, PASSWORD = {password}")

sesja = SessionXTB(main_address = f"wss://ws.xtb.com/demo", stream_address = f"wss://ws.xtb.com/demoStream")
sesja.login(username, password)
print(sesja.getCandles("EURUSD"))