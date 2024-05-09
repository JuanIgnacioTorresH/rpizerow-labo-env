import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Ata el socket a una dirección de O´y puerto especifico
    s.bind((HOST, PORT))
    # Acepta una sola conexión
    s.listen(1)
    # Acepta una conexion, devuelve el socket que representa al ciente y la dirección del cliente
    client, addr = s.accept()
    with client:
        print('Connected by', addr)
        while True:
            # Recibo
            data = client.recv(1024)
            # Devuelvo
            client.sendall(data)