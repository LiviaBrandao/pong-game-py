 
class Raquete:
    def __init__(self, color, width, height, x):
        self.color  = color
        self.width  = width
        self.height = height

        self.y = 150
        self.x = x

        self.D = False
        self.C = False
        self.E = True
        self.B = True


    def moverParaCima(self):
      if self.y > 1:
          self.y -= 1
    
    def moverParaBaixo(self):
      if self.y < 400:
          self.y += 1

          
          
    

