#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import zmq
import json

def main():
    # curr server address
    server_addr="tcp://*:3333"
    context_client = zmq.Context()
    client_socket = context_client.socket(zmq.REP)
    client_socket.bind(server_addr)
    
    #  Socket to talk to registry server
    context = zmq.Context()
    print("Requesting registery server")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    #  Request registry server
    list=["register",server_addr]
    socket.send_string(json.dumps(list))
    message = socket.recv()
    m=message.decode()
    print(f"Received reply [ {m} ]")
    while(True):
        client_request = json.loads(client_socket.recv_string())




if __name__ == "__main__":
    main()