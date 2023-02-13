
import socket
from socket import SHUT_RDWR
import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65434 # Port to listen on (non-privileged ports are > 1023)

# Define socket paramaters.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allows the socket to be reused in the event of a crash.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket and listen for incoming connections.
s.bind((HOST, PORT))
s.listen()

def generateCSVString(data):
    dates = []
    highs = []
    csv = []

    # Store the stock dates in the date list.
    for entry in data.index:
        dates.append(str(entry.date()).replace('-',',') + ',')

    # Store the stock highs  
    for entry in data.values.tolist():
        highs.append(str(round(entry[1], ndigits=3)) + '\n')

    # Concatenate the string data together.
    for i in range(0, len(dates)):
        csv.append(dates[i] + highs[i])
    
    return ''.join(csv)

while True:
    
    try:
        # Wait until a client connects.
        conn, addr = s.accept()

        # Print a connection message showing the client address.
        print(f"Connected by {addr}")

        # Decode the stock symbol from the client.
        stock_symbol = conn.recv(1024).decode()

        # Print out the symbol recieved.
        print('Recieved the stock symbol ' + str(stock_symbol) +'.')

        # Calculate the date for one year ago.
        one_year_ago = datetime.now() - relativedelta(years=1)

        # Query yFinance for the last year of stock information.
        data = yf.Ticker(stock_symbol).history(period='1d', start=one_year_ago)
        
        # Join the string list together and send it back to the client.
        conn.send(bytes(generateCSVString(data), 'utf-8'))

        # Close the connection.
        conn.close()
    except:
        print("An error has occured.")
        exit()

