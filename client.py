import socket


def run_client():
    """
    # create socket object
    socket.AF_INET specifies the IP address family for IPv4
    socket.SOCK_STREAM indicates that we are using TCP connection
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"  # server ip address
    server_port = 8000  # server port number

    """
    # connect client to server
    connect automatically chooses a free port and picks an ip address with the best route to the server from the
    system’s network interfaces which is 127.0.0.1 in this case
    """
    client.connect((server_ip, server_port))

    try:
        while True:
            # input message and send it to the server
            msg = input("Enter message: ")
            client.send(msg.encode("utf-8")[:1024])

            # handling server response
            response = client.recv(1024)
            response = response.decode("utf-8")

            # break out of loop if payload message from server is "closed"
            if response.lower() == "closed":
                break

            print(f"Received: {response}")
    except Exception as e:
        print(f"Client Socket Error: {e}")
    finally:
        # close connection to server: this helps free up resources used
        client.close()
        print(f"Connection to server closed")


run_client()
