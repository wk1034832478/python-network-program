import socket
#创建套接字对象
s = socket.socket()

host = socket.gethostname()
port = 1234 

s.connect((host, port))
print( s.recv(1024) )