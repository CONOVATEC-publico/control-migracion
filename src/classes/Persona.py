class Persona:
  def __init__(
      self, 
      nombres, 
      apellidos, 
      genero, 
      fechaNacimiento, 
      numeroIdentificacion,
      nacionalidad, 
      direccion, 
      telefono
    ):
    self.nombres = nombres
    self.apellidos = apellidos
    self.genero = genero
    self.fechaNacimiento = fechaNacimiento
    self.numeroIdentificacion = numeroIdentificacion
    self.nacionalidad = nacionalidad
    self.direccion = direccion
    self.telefono = telefono

  def getNombres(self):
    return self.nombres
  
  def setNombres(self, nombres):
    self.nombres = nombres

  def getApellidos(self):
    return self.apellidos
  
  def setApellidos(self, apellidos):
    self.apellidos = apellidos

  def getGenero(self):
    return self.genero
  
  def setGenero(self, genero):
    self.genero = genero

  def getFechaNacimiento(self):
    return self.fechaNacimiento
  
  def setFechaNacimiento(self, fechaNacimiento):
    self.fechaNacimiento = fechaNacimiento

  def getNumeroIdentificacion(self):
    return self.numeroIdentificacion
  
  def setNumeroIdentificacion(self, numeroIdentificacion):
    self.numeroIdentificacion = numeroIdentificacion

  # def getNumeroPasaporte(self):
  #   return self.numeroPasaporte
  
  # def setNumeroPasaporte(self, numeroPasaporte):
  #   self.numeroPasaporte = numeroPasaporte

  def getNacionalidad(self):
    return self.nacionalidad
  
  def setNacionalidad(self, nacionalidad):
    self.nacionalidad = nacionalidad

  def getDireccion(self):
    return self.direccion
  
  def setDireccion(self, direccion):
    self.direccion = direccion
  
  def getTelefono(self):
    return self.telefono
  
  def setTelefono(self, telefono):
    self.telefono = telefono

