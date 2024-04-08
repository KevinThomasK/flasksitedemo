import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.bind((HOST_NAME, PORT))
s.listen(4)

while True:
    client, address = s.accept()
    client.send(bytes("hello .. How are you ?", "utf-8"))
    print('client is connected and has address ', address)
