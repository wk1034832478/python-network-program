import socket
#创建套接字对象
s = socket.socket()

host = socket.gethostname()
port = 1234 
s.bind((host, port))

# 设置最大连接数
s.listen(5)

while True:
	con, addr = s.accept()
	print( 'get connection, address:', addr )
	con.send(b'hello, welcome')
	#con.close()
