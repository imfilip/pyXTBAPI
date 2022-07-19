from src.api import SessionXTB
import time


with open("src/secrets.txt") as f:
    lines = f.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    print(f"USERNAME = {username}, PASSWORD = {password}")

connection_XTB = SessionXTB(main_address = f"wss://ws.xtb.com/demo", stream_address = f"wss://ws.xtb.com/demoStream")

print(connection_XTB)
connection_XTB.login(username, password)
print(connection_XTB.session_id)

### From demoStream session ###

print("====== getBalance ======")
print(connection_XTB.getBalance())

time.sleep(1)

print("====== getCandles ======")
print(connection_XTB.getCandles("BITCOIN"))

time.sleep(1)

print("====== getKeepAlive ======")
print(connection_XTB.getKeepAlive())

# time.sleep(1)

# print("====== getNews ======")
# print(connection_XTB.getNews())

time.sleep(1)

print("====== getProfits ======")
print(connection_XTB.getProfits())

time.sleep(1)

print("====== getTickPrices ======")
print(connection_XTB.getTickPrices("BITCOIN"))

time.sleep(1)


### From demo session ###

print("====== getAllSymbols ======")
print(connection_XTB.getAllSymbols())

time.sleep(1)

connection_XTB.logout()
