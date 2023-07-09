class Usuario:
    # Estático
    numeroUsuario = 0

    # Principal objetos
    def __init__(self):
        self.__tipoUsuario = input("Ingrese el tipo de usuario: ")
        self.__numeroPasaporte = input("Ingrese el número de pasaporte: ")
        self.__numeroIdentificacion = input("Ingrese el número de identificación: ")
        self.__nombreCompleto = input("Ingrese el nombre completo: ")
        self.__anhoNacimiento = input("Ingrese el año de nacimiento: ")
        self.__paisOrigen = input("Ingrese el país de origen: ")
        self.__nombreContactoPaisOrigen = input("Ingrese el nombre de contacto en el país de origen: ")
        self.__nombreContactoPaisDestino = input("Ingrese el nombre de contacto en el país de destino: ")
        self.__telefonoContactoPaisOrigen = input("Ingrese el teléfono de contacto en el país de origen: ")
        self.__telefonoContactoPaisDestino = input("Ingrese el teléfono de contacto en el país de destino: ")
        self.__reservaLugarDestino = input("Ingrese la reserva del lugar de destino: ")
        self.__direccionLugarDestino = input("Ingrese la dirección del lugar de destino: ")
        self.__boletoSalida = input("Ingrese el número de boleto de salida: ")
        Usuario.numeroUsuario += 1

# Obtener cantidad de usuarios a generar desde el usuario
cantidad_usuarios = int(input("Ingrese la cantidad de usuarios que desea generar: "))

# Generar usuarios
usuarios = []
for _ in range(cantidad_usuarios):
    usuario = Usuario()
    usuarios.append(usuario)

# Imprimir el número de usuarios generados
print("Se generaron" + Usuario.numeroUsuario + "usuarios.")
