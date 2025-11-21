import socket

hostIP = "192.168.3.116"
port = 8888


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((hostIP, port))
print("[*] connected to server, Message sent")

msg = client.recv(1024)
print(f"Message from Server: {msg.decode()}")



client.close()