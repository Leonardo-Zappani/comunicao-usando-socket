import socket

# Criado por Leonardo Zappani 25/05/23

# Define as configurações do servidor
HOST = 'localhost'  # Endereço IP do servidor
PORT = 12345  # Porta utilizada pelo servidor

# Cria o socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))

# Inicia o servidor
servidor.listen(1)
print('Servidor aguardando conexão...')

# Aceita a conexão do cliente
conexao, endereco = servidor.accept()
print('Cliente conectado:', endereco)

while True:
    # Recebe a mensagem do cliente
    mensagem = conexao.recv(1024).decode()
    if not mensagem:
        break

    print('Mensagem recebida do cliente:', mensagem)

    # Envie uma resposta de confirmação ao usuário
    resposta = 'Recebido: ' + mensagem
    conexao.send(resposta.encode())

# Fecha a conexão
conexao.close()
