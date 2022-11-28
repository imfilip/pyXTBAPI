from websocket import create_connection
import json

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

class SessionXTB():
    
    session_id = None
    connection_status = None

    def __init__(self, main_address, stream_address):
        self.main_session = create_connection(main_address)
        self.stream_session = create_connection(stream_address)

    def send_JSON(self, data_dict, session_type):
        if session_type == "stream":
            session = self.stream_session
        else:
            session = self.main_session

        data = json.dumps(data_dict)
        session.send(data)
        response = json.loads(session.recv())
        return response

    def login(self, user_id, password):
        data_dict = {"command": "login", "arguments": {"userId": user_id, "password": password}}
        response = self.send_JSON(data_dict, "main")
        self.session_id = response["streamSessionId"]
        self.connection_status = response["status"]
        print(bcolors.OKGREEN + bcolors.BOLD + str(response["status"]) + bcolors.ENDC)
        return response

    def logout(self):
        data_dict = {"command": "logout"}
        response = self.send_JSON(data_dict, "main")
        print(bcolors.FAIL + bcolors.BOLD + str(response["status"]) + bcolors.ENDC)
        return response

    ### Interactions with streaming server ###
    ### Na potrzeby pozyskiwania płynnych danych (balance, itp.) należy korzystać 
    # ze specjalnego połączenia - właśnie demoStream.
    
    def getBalance(self):
        data_dict = {"command": "getBalance", "streamSessionId": self.session_id}
        response = self.send_JSON(data_dict, "stream")
        return response

    def getCandles(self, symbol):
        data_dict = {"command": "getCandles", "streamSessionId": self.session_id, "symbol": symbol}
        response = self.send_JSON(data_dict, "stream")
        return response

    def getKeepAlive(self):
        data_dict = {"command": "getKeepAlive", "streamSessionId": self.session_id}
        response = self.send_JSON(data_dict, "stream")
        return response
    
    def getNews(self):
        data_dict = {"command": "getNews ", "streamSessionId": self.session_id}
        response = self.send_JSON(data_dict, "stream")
        return response
    
    def getProfits(self):
        data_dict = {"command": "getProfits", "streamSessionId": self.session_id}
        response = self.send_JSON(data_dict, "stream")
        return response

    def getTickPrices(self, symbol, minArrivalTime = 5000, maxLevel = 2):
        data_dict = {"command": "getTickPrices", 
                     "streamSessionId": self.session_id, 
                     "symbol": symbol,
                     "minArrivalTime": minArrivalTime,
                     "maxLevel": maxLevel}
        response = self.send_JSON(data_dict, "stream")
        return response

    def getTrades(self):
        data_dict = {"command": "getTrades", "streamSessionId": self.session_id}
        response = self.send_JSON(data_dict, "stream")
        return response

    def ping(self):
        data_dict = {"command": "ping", "streamSessionId": self.session_id}
        response = self.send_JSON(data_dict, "stream")
        return response

    ### Interactions with main server ###
    ### Tutaj raczej mam doczynienia ze statycznymi danymi, stąd inne połączenie.
    
    def getAllSymbols(self):
        data_dict = {"command":"getAllSymbols"}
        response = self.send_JSON(data_dict, "main")
        return response





