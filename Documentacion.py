class Usuario:



    def __init__(self,tipoUsuario,numeroPasaporte,numeroIdentificacion,nombreCompleto,anhoNacimiento,paisOrigen,nombreContactoPaisOrigen,nombreContactoPaisDestino,telefonoContactoPaisOrigen,telefonoContactoPaisDestino,reservaLugarDestino,direccionLugarDestino,boletoSalida):
        self.tipoUsuario = tipoUsuario
        self.numeroPasaporte = numeroPasaporte
        self.numeroIdentificacion = numeroIdentificacion
        self.nombreCompleto = nombreCompleto
        self.anhoNacimiento = anhoNacimiento
        self.paisOrigen = paisOrigen
        self.nombreContactoPaisOrigen = nombreContactoPaisOrigen
        self.nombreContactoPaisDestino = nombreContactoPaisDestino
        self.telefonoContactoPaisOrigen = telefonoContactoPaisOrigen
        self.telefonoContactoPaisDestino = telefonoContactoPaisDestino
        self.reservaLugarDestino = reservaLugarDestino
        self.direccionLugarDestino = direccionLugarDestino
        self.boletoSalida = boletoSalida

#Funciones para mostrarle al usuario los datos ingresados
    def get_tipoUsuario (self):
        print(f"Su tipo usuario es: {self.tipoUsuario}")
    def get_numeroPasaporte (self):
        print(f"Su número de pasaporte es: {self.numeroPasaporte}")
    def get_numeroIdentificacion (self):
        print(f"El número de identificación digitado de su País de origen es: {self.numeroIdentificacion}")
    def get_anhoNacimiento (self):
        print(f"Su año de nacimiento es: {self.anhoNacimiento}")
    def get_paisOrigen (self):
        print(f"Su país de origen es: {self.paisOrigen}")
    def get_nombreContactoPaisOrigen (self):
        print(f"El nombre de la persona que respalda su identidad en su país de origen es: {self.nombreContactoPaisOrigen}")
    def get_telefonoContactoPaisOrigen (self):
        print(f"El número de teléfono de la persona que respalda su identidad en su país de origen es: {self.telefonoContactoPaisOrigen}")
    def get_nombreContactoPaisDestino (self):
        print(f"El nombre de la persona que respalda su identidad en el país de su destino es: {self.nombreContactoPaisDestino}")
    def get_telefonoContactoPaisDestino (self):
        print(f"El número de teléfono de la persona que respalda su identidad en el país de su destino: {self.telefonoContactoPaisDestino}")
    def get_reservaLugarDestino (self):
        print(f"El código de la reserva en donde se hospedará es (también puede ser familia o particular): {self.reservaLugarDestino}")
    def get_direccionLugarDestino (self):
        print(f"La dirección del lugar en donde se hospedará es: {self.direccionLugarDestino}")
    def get_boletoSalida (self):
        print(f"El código del boleto que usó es: {self.boletoSalida}")

#Se definen las condiciones para la digitación de los datos del Usuario
    def set_tipoUsuario (self):
        input(f"Digite su tipo usuario: {self.tipoUsuario}")
    def set_numeroPasaporte (self):
        input(f"Digite su número de pasaporte: {self.numeroPasaporte}")
    def set_numeroIdentificacion (self):
        input(f"Digite el número de identificación del documento de su País de origen{self.numeroIdentificacion}")
    def set_anhoNacimiento (self):
        input(f"Digite su año de nacimiento: {self.anhoNacimiento}")
    def set_paisOrigen (self):
        input(f"Digite su país de origen: {self.paisOrigen}")
    def set_nombreContactoPaisOrigen (self):
        input(f"Digite el nombre completo de una persona que respalde su identidad en su país de origen, de preferencia un familiar: {self.nombreContactoPaisOrigen}")
    def set_telefonoContactoPaisOrigen (self):
        input(f"Digite el número de la persona que respalde su identidad en su país de origen: {self.telefonoContactoPaisOrigen}")
    def set_nombreContactoPaisDestino (self):
        input(f"Digite el nombre completo de una persona que respalde su identidad en el país de destino que se dirige, de preferencia un familiar: {self.nombreContactoPaisDestino}")
    def set_telefonoContactoPaisDestino (self):
        input(f"El número de teléfono de la persona que respalda su identidad en el país de su destino: {self.telefonoContactoPaisDestino}")
    def set_reservaLugarDestino (self):
        input(f"Digite el código de la reserva que tiene hecha en el lugar en donde se hospedará, si esta es un familiar escribir la misma palabra y si es otra particular escribir también dicha palabra: {self.reservaLugarDestino}")
    def set_direccionLugarDestino (self):
        input(f"Digite la dirección del lugar en donde se hospedará, el orden debe ser Ciudad, Barrio, Dirección: {self.direccionLugarDestino}")
    def set_boletoSalida (self):
        input(f"Digite el código del boleto que tomó ya sea de avión, barco o autobus: {self.boletoSalida}")
        
        
Usuario.set_tipoUsuario()
Usuario.set_numeroPasaporte()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()
Usuario.set_tipoUsuario()