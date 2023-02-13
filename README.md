# Communication Contract

My Stock Microservice requires a client socket connection to access. The file microservice_query_example.py provides a script to return a CSV file containing the last calender year of stock highs per day. The file is hardcoded to request Meta's stock highs, but theoretically it could be used to pull any stock.

To request data, connect to the hardcoded host and port (currently the loopback address on port 65434) and send a string containing the symbol of the stock you want data from.

To retrieve the data, simply read from the socket when data is available. An example call is listed below in Python:

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"META")
    data = s.recv(65536)

![image failed to load.](blob:null/11780d2f-7119-46c9-afbe-29d7b21b8518)
