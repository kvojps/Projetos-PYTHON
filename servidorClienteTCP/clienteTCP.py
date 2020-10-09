import socket

host_name = socket.gethostname()
protocolo = socket.gethostbyname(host_name)

alvo_host = protocolo
porta_alvo = 80

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((alvo_host,porta_alvo))
#Enviar mensagem para o servidor
cliente.send(b'Conecto-me ao servidor')
resposta = cliente.recv(4096)
print(resposta)