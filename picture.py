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
    return Picture(vertical)

  def horizontalMirror(self):
    nuevo = []
    for x in range(len(self.img)):
      nuevo.append(self.img[(len(self.img) - 1) - x])
    return Picture(nuevo)

  def negative(self):  
    nuevo = []
    for x in range(len(self.img)):
      cadena = ""
      for y in range(len(self.img[x])):
        cadena += self._invColor(self.img[x][y])
      nuevo.append(cadena)
    return Picture(nuevo)


  def join(self, p):
    nuevo = []
    for x in range(len(self.img)):     # Iterar sobre los elementos de la imagen actual
        nuevo.append(self.img[x] + p.img[x])
    return Picture(nuevo)

  def up(self, p):
    nuevo = []
    for x in range(len(self.img)): 
      cadena = ""
      for y in range(len(self.img[x])):
        if(self.img[x][y] != " "):
          cadena += self.img[x][y]
        else: 
          cadena += p.img[x][y]
      nuevo.append(cadena)
    return Picture(nuevo)

  def under(self, p):
    nuevo = [] # Crear una nueva imagen con la concatenación de ambas
    for x in range(len(self.img)):     # Iterar sobre los elementos de la imagen actual
        nuevo.append(self.img[x])     # Copiar los elementos de la imagen actual
    for y in range(len(p.img)):        # Iterar sobre los elementos de la imagen p
        nuevo.append(p.img[y])  # Colocar los elementos de la imagen p debajo
    return Picture(nuevo)                       # Retornar la nueva imagen compuesta

  
  def horizontalRepeat(self, n):
    nuevo = []
    if(n == 1):
      return self
    else:
      for x in range(len(self.img)): 
        nuevo.append(self.img[x] * n)
      return Picture(nuevo)

  def verticalRepeat(self, n):
    nuevo = []
    if(n == 1):
      return self
    else:
      for i in range(n):
        for x in range(len(self.img)): 
          nuevo.append(self.img[x])     
      return Picture(nuevo)

  #Extra: Sólo para realmente viciosos 
  def rotate(self): 
    nuevo = []
    for x in range(len(self.img)):
      cadena = ""
      for y in range(len(self.img[x])):
        cadena += self.img[-y][x]
      nuevo.append(cadena)
    return Picture(nuevo)

