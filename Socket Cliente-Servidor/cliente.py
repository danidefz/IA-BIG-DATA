import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost',12345))

try:
    
    #enviamos datos
    
    mensaje = 'Hola servidor'.encode()
    cliente.sendall(mensaje)
    
    #recibimos datos del servidor
    respuesta = cliente.recv(1024)
    print('Respuesta del servidor:' , respuesta.decode())
    
finally:
    
    cliente.close()
    
    
    