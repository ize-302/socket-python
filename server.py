import socket


def run_server():
    """
    # create socker object
    socket.AF_INET specifies the IP address family for IPv4
    socket.SOCK_STREAM indicates that we are using TCP connection
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # define ip address and port
    ip_address = "127.0.0.1"
    port = 8000

    try:
        # bind server socket to specific ip address and port
        server.bind((ip_address, port))

        # listen for incoming connection
        server.listen(0)
        print(f"Server listening on {ip_address}:{port}")

        # accept incoming connections
        client_socket, client_address = server.accept()
        print(f"Connection from {client_address[0]}:{client_address[1]} has been accepted")

        # receive data from client
        while True:
            request = client_socket.recv(1024)
            request = request.decode("utf-8")

            # break the look if we recieve message "close" from the client
            if request.lower() == "close":
                client_socket.send("closed".encode("utf-8"))
                break

            print(f"Received: {request}")

        # close socket connection we have with client
        client_socket.close()
    except Exception as e:
        print(f"Server Socket Error: {e}")
    finally:
        print(f"Connection to client has been closed")
        server.close()


run_server()
