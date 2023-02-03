#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import json

 
def register(servers,addr,curr_server_count,max_server):
    if(curr_server_count<max_server):
        servers.append(addr)
        return "server registered"
    else:
        return "max server limit reached"
    

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    servers=[]
    max_server=1
    curr_server_count=0
    while True:
    #  Wait for next request from client

        message = json.loads(socket.recv_string())
        
        # register request
        if(message[0]=="register"):
            reply=register(servers,message[1],curr_server_count,max_server)
            if(reply=="server registered"):
                curr_server_count+=1
            socket.send_string(reply)


        
        # print(f"Received request: {message}")

        print(servers)
        print(curr_server_count)

        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        

if __name__ == "__main__":
    main()