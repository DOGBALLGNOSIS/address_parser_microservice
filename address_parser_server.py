import zmq
import json

def parse_address(address):
    street, city_state_zip = address.split(', ', 1)
    city, state_zip = city_state_zip.rsplit(', ', 1)
    state, zip_code = state_zip.split(' ', 1)
    return {
        "Street Address": street,
        "City": city,
        "State": state,
        "Zip Code": zip_code
    }

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv_json()
        address = message.get('address')
        
        response = parse_address(address) if address else {"error": "Address not provided"}
        
        socket.send_json(response)

if __name__ == "__main__":
    main()