#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
# pyhton3 server.py
import zmq
import json


def main():
    context = zmq.Context()

    #  Socket to talk to registry server
    print("Connecting to registry server")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    #  Do 10 requests, waiting each time for a response


    list=["1","2","3"]
    socket.send_string(json.dumps(list))

    #  Get the reply.

    message = socket.recv()
    m=message.decode()
    print(f"Received reply [ {m} ]")


if __name__ == "__main__":
    main()