import socket

host_name = socket.gethostname()
#A função gethostbyname recupera informações do host correspondentes ao nome do host.
protocolo = socket.gethostbyname(host_name)

print('Endereço de IP: '+protocolo)
