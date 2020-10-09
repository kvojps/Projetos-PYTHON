import socket
import threading

#Obtenção do IP
host_name = socket.gethostname()
protocolo = socket.gethostbyname(host_name)

# Local onde o servidor vai rodar
endereço = protocolo
porta = 80

# O primeiro parâmetro refere-se ao protocolo ipv4, já o segundo faz referência ao protocolo TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((endereço, porta))
servidor.listen(5)  # Ouvir 5 conexões simultâneas
print(f'Escutando {endereço}:{porta}')


def comunicar_cliente(client_socket):
    requisicao = client_socket.recv(1024)
    print(f'Recebido: {requisicao}')
    print('-' * 30)
    client_socket.send(b'Mensagem recebida')
    client_socket.close()



while True:
    client, addr = servidor.accept()
    print(f'Conexão aceita de: {addr[0]}:{addr[1]}')
    client_handler = threading.Thread(target=comunicar_cliente(client))
    client_handler.start()
