import socket

#Creamos un servidor TcP

#servidor utilizando conexiones IPV4(AF_INET) y que queremos que sean TCP(SOCK.STREAM)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Asignamos el socket a una direccion local donde va a estar escuchando las comunicaciones y a un puerto
servidor.bind(('localhost' , 12345))

#Empieza a escuchar conexiones
servidor.listen()
print('esperando conexiones')

#Acepta una conexion si alguien intenta conectarse a nosotros
#Este metodo nos devuelve dos cosas. un objeto conexion que vamos a utilizar para recibir y enviar informacion, y tambien la direccdion del sistema que se esta conectando a nosotros
conexion, direccion = servidor.accept()


#Procesando los datos que nos envian y responder (Rescuerdo que esto es un servidor)

with conexion:
    print('Conectado a : ' , direccion)
    while True:
        datos = conexion.recv(1024)
        if not datos:
            break
        print(f'Datos recibidos del cliente: {datos.decode()}')
        mensaje = 'Hola Cliente'.encode()
        conexion.sendall(mensaje)
        
conexion.close()

        
        
""""""      
        
#Esto es un servidor MUY BASICO, que lo que esta haciendo es recibir conexiones a esta direccion y a este puerto, cuando recibe la conexion muestra los datos que nos ha enviado el cliente, y
#lo responde con el mensaje.
        


""""""




