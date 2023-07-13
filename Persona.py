class Persona:
  def __init__(self, nombres, apellidos, genero, fecha_nacimiento, dni,
                nacionalidad, direccion, telefono):
    self.nombres = nombres
    self.apellidos = apellidos
    self.genero = genero
    self.fecha_nacimiento = fecha_nacimiento
    self.dni = dni
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
    return self.fecha_nacimiento
  
  def setFechaNacimiento(self, fecha_nacimiento):
    self.fecha_nacimiento = fecha_nacimiento

  def getDni(self):
    return self.dni
  
  def setDni(self, dni):
    self.dni = dni

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

