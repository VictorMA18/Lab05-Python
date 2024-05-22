from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return BLACK
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    nuevo = []
    for x in range(len(self.img)):
      nuevo.append(self.img[(len(self.img) - 1) - x])
    return nuevo

  def negative(self):  
    for x in range(len(self.img)):
      cadena = ""
      for y in range(len(self.img[x])):
        cadena += self._invColor(self.img[x][y])
      self.img[x] = cadena
    return self


  def join(self, p):
    nuevo = []
    for x in range(len(self.img)):     # Iterar sobre los elementos de la imagen actual
        nuevo.append(self.img[x] + p.img[x])
    return nuevo

  def up(self, p):
    nuevo = []
    for x in range(len(self.img)): 
      cadena = ""
      for y in range(len(self.img[x])):
        if(self.img[x][y] != " "):
          cadena += self.img[x][y]
        else: 
          cadena += p.img[x][y]
      print(cadena)
      nuevo.append(cadena)
    return nuevo

  def under(self, p):
    nuevo = [] # Crear una nueva imagen con la concatenación de ambas
    for x in range(len(self.img)):     # Iterar sobre los elementos de la imagen actual
        nuevo.append(self.img[x])     # Copiar los elementos de la imagen actual
    for y in range(len(p.img)):        # Iterar sobre los elementos de la imagen p
        nuevo.append(p.img[y])  # Colocar los elementos de la imagen p debajo
    return nuevo                       # Retornar la nueva imagen compuesta

  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

