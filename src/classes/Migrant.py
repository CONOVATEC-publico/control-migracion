from classes.Persona import Persona

class Migrant(Persona):
  def __init__(
    self,
    nombres,
    apellidos,
    genero,
    fechaNacimiento,
    numeroIdentificacion,
    numeroPasaporte,
    nacionalidad,
    direccion,
    telefono,
    direccionPaisOrigen,
    nombreContactoPaisOrigen,
    telefonoContactoPaisOrigen,
    nombreContactoPaisDestino,
    telefonoContactoPaisDestino,
    indiceDeRiesgo,
    ingresoAprobado,
  ):
    super().__init__(
      nombres,
      apellidos,
      genero,
      fechaNacimiento,
      numeroIdentificacion,
      numeroPasaporte,
      nacionalidad,
      direccion,
      telefono,
    )
    self.direccionPaisOrigen = direccionPaisOrigen
    self.nombreContactoPaisOrigen = nombreContactoPaisOrigen
    self.telefonoContactoPaisOrigen = telefonoContactoPaisOrigen
    self.nombreContactoPaisDestino = nombreContactoPaisDestino
    self.telefonoContactoPaisDestino = telefonoContactoPaisDestino
    self.indiceDeRiesgo = indiceDeRiesgo
    self.ingresoAprobado = ingresoAprobado

  def getDireccionPaisOrigen(self):
    return self.direccionPaisOrigen

  def setDireccionPaisOrigen(self, direccionPaisOrigen):
    self.direccionPaisOrigen = direccionPaisOrigen

  def getNombreContactoPaisOrigen(self):
    return self.nombreContactoPaisOrigen

  def setNombreContactoPaisOrigen(self, nombreContactoPaisOrigen):
    self.nombreContactoPaisOrigen = nombreContactoPaisOrigen

  def getTelefonoContactoPaisOrigen(self):
    return self.telefonoContactoPaisOrigen

  def setTelefonoContactoPaisOrigen(self, telefonoContactoPaisOrigen):
    self.telefonoContactoPaisOrigen = telefonoContactoPaisOrigen

  def getNombreContactoPaisDestino(self):
    return self.nombreContactoPaisDestino

  def setNombreContactoPaisDestino(self, nombreContactoPaisDestino):
    self.nombreContactoPaisDestino = nombreContactoPaisDestino

  def getTelefonoContactoPaisDestino(self):
    return self.telefonoContactoPaisDestino

  def setTelefonoContactoPaisDestino(self, telefonoContactoPaisDestino):
    self.telefonoContactoPaisDestino = telefonoContactoPaisDestino

  def getIndiceDeRiesgo(self):
    return self.indiceDeRiesgo

  def setIndiceDeRiesgo(self, indiceDeRiesgo):
    self.indiceDeRiesgo = indiceDeRiesgo
      
  def getIngresoAprobado(self):
    return self.ingresoAprobado

  def setIngresoAprobado(self, ingresoAprobado):
    self.ingresoAprobado = ingresoAprobado


