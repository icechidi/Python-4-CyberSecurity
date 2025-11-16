import socket

SERVERIP = "192.168.3.116"
SERVERPORT = 8888

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((SERVERIP, SERVERPORT))

server.listen(5)

print(f"[*] Server is Listening at port {SERVERPORT}")
conn, addr = server.accept()

print(f"[*] Connection established from {addr}")
conn.send(b"Hello from Server")



conn.close()
server.close()