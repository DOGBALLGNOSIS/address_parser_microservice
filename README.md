# address_parser_microservice
Overview:

This microservice parses an address into its components: street address, city, state, and zip code. The microservice uses ZeroMQ for communication.


Request Data
------------

- URL: tcp://localhost:5555
- Protocol: ZeroMQ
- Request Format: JSON
- Response Format: JSON


To programmatically request data from the microservice, connect to the socket and send a JSON request with an "address" field. Reference the demo for an example! ^.^