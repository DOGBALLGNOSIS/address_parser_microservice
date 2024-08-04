import zmq
import json

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    address = "123 Test, Portland, OR 12345"
    socket.send_json({"address": address})

    response = socket.recv_json()
    print("Parsed Address:", json.dumps(response, indent=4))

if __name__ == "__main__":
    main()
