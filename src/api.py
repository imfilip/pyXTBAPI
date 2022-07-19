from websocket import create_connection
import json



class SessionXTB():
    
    session_id = None
    connection_status = None

    def __init__(self, main_address, stream_address):
        self.main_session = create_connection(main_address)
        self.stream_session = create_connection(stream_address)

    def send_JSON_data(self, data_dict, session_type):
        if str(session_type).lower == "stream":
            session = self.stream_session
        else:
            session = self.main_session

        data = json.dumps(data_dict)
        session.send(data)
        response = json.loads(session.recv())
        return response

    def login(self, user_id, password):
        data_dict = {'command': 'login', 'arguments': {'userId': user_id, 'password': password}}
        response = self.send_JSON_data(data_dict, "main")
        self.session_id = response["streamSessionId"]
        self.connection_status = response["status"]
        print(response["status"])
        return response

    ### Interactions with streaming server ###

    def getBalance

