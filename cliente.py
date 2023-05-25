import socket

# Criado por Leonardo Zappani 25/05/23

# Define as configurações do cliente
HOST = 'localhost'  # Endereço IP do servidor
PORT = 12345  # Porta utilizada pelo servidor

# Cria o socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
cliente.connect((HOST, PORT))
print('Conexão estabelecida com o servidor')

while True:
    # Digite uma mensagem para enviar ao servidor
    mensagem = input('Digite uma mensagem (ou "sair" para encerrar): ')
    if mensagem.lower() == 'sair':
        break

    # Envie a mensagem para o servidor
    cliente.send(mensagem.encode())

    # Recebe a resposta do servidor
    resposta = cliente.recv(1024).decode()
    print('Resposta do servidor:', resposta)

# Fecha a conexão
cliente.close()
