import socket
import psutil
import pickle

end = socket.gethostname()
porta = 9999
bufferSize = 1024

msg_servidor = 'Conectado'
bytesToSend = str.encode(msg_servidor)

info_disco = psutil.virtual_memory()
envio_bytes = pickle.dumps(info_disco)

servidor_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

servidor_socket.bind((end, porta))

print('Aguardando conexão')

while True:
    endereco_par = servidor_socket.recvfrom(bufferSize)
    mensagem = endereco_par[0].decode('ascii')
    endereco = endereco_par[1]

    msg_cliente = f'Cliente:{mensagem}'
    ip_cliente = f'Endereço cliente:{endereco}'

    print(msg_cliente)
    print(ip_cliente)

    servidor_socket.sendto(envio_bytes, endereco)