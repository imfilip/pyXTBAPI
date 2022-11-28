from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from twisted.internet import reactor


# Source: https://github.com/crossbario/autobahn-python
class MyServerProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))
    
    def onOpen(self):
        print("WebSocket connection open")
    
    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {} bytes".format(len(payload)))
        else:
            print("Text message received: {}".format(payload.decode("utf-8")))
        
        self.sendMessage(payload, isBinary)
    
    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))


if __name__ == "__main__":
    factory = WebSocketServerFactory()
    factory.protocol = MyServerProtocol

    reactor.listenTCP(, factory)
    reactor.run()