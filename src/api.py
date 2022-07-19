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

    def getBalance(self):
        data_dict = {"command": "getBalance", "streamSessionId": self.session_id}
        response = self.send_JSON(data_dict, "stream")
        return response

    



