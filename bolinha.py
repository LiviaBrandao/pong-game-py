from random import randint

class Bolinha :

    def __init__ (self, color, radium, alturaJanela, larguraJanela) :
        self.color    = color
        self.radium   = radium

        self.x = 0
        self.y = 0

        self.D = False
        self.C = False
        self.E = True
        self.B = True

        self.alturaJanela  = alturaJanela
        self.larguraJanela = larguraJanela

    def mover (self):

        if self.B :
            self.y += 1

        if self.D :
            self.x += 1

        if self.E :
            self.x -= 1

        if self.C :
            self.y -= 1

    def meOrienta (self, r1, r2):
        #estou verificando o eixo Y da raquete
        if self.x == r1.x:
            if self.y >= r1.y and self.y <= (r1.height / 2) + r1.y : #da metade pra cima
                return 1
            elif self.y <= r1.height + r1.y and self.y > (r1.height / 2) + r1.y : #da metade pra baixo
                return -1 
        if self.x == r2.width:
            if self.y >= r2.y and self.y <= (r2.height / 2) + r2.y : #da metade pra cima
                return 2
            elif self.y <= r2.y + r2.height and self.y > (r2.height / 2) + r2.y :
                return -2
        return 0

    def colisao (self, r1, r2) :
        ret = self.meOrienta(r1, r2)
        print ("retorno", ret)

        if ret == 0 :
            if self.y <= 0 :
                self.B = True
                self.C = False

            if self.x >= self.larguraJanela :
                self.D = False
                self.E = True

            if self.x <= 0 :
                self.D = True
                self.E = False

            if self.y >= self.alturaJanela :
               self.C = True
               self.B = False
        else :
            if ret == -1 : 
                self.C = self.E = True
                self.B = self.D = False

            if ret == 1 :
                self.B = self.E = True
                self.C = self.D = False

            if ret == -2:
               self.C = self.D = True
               self.B = self.E = False

            if ret == 2:
               self.B = self.D = True
               self.C = self.E = False




             
          


