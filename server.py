import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345
s.bind((host,port))
s.listen(5)
print("Socket is listening")
conn, addr = s.accept()
print("Got a connection from", addr)


while True:
    data = input("Server:")
    conn.sendall(data.encode())
    data = conn.recv(1024)
    print(addr,":",data.decode())
    