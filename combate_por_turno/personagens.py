from time import sleep

class Entidade:
      def __init__(self, vida, energia):
            self.vida = vida
            self.energia = energia
      
      def estar_vivo(self):
            return self.vida > 0
          

class player(Entidade):
      def __init__(self):
            super().__init__(vida=100, energia=100)
      
      def atacar(self):
            custo = 20
            if self.energia >= custo:
                  laplace.vida -= 15
                  self.energia -= custo
                  print('     -')
                  print('     Jogador atacou Laplace!')
                  print('     Laplace perdeu 15 de vida.')
                  print('     -20 de energia.')
            else:
                  print('     O jogador não tem energia o suficiente.')
                  print('     Você está cansado.')
            sleep(2)
      

      def meditar(self):
            valor = 40
            self.energia += valor if self.energia + valor < 100 else 100 - self.energia
            print('     -')
            print('     O jogador meditou.')
            print('     Recuperou sua energia.')
            sleep(3)
      
      def regenerar(self):
            valor = 30
            custo = 30
            if self.energia >= custo:
                  self.vida += valor if self.vida + valor < 100 else 100 - self.vida
                  self.energia -= custo
                  print('     -')
                  print('     O jogador se regenerou.')
                  print('     Recuperou sua parte de sua vida.')
            else:
                  print('     O jogador não tem energia o suficiente.')
                  print('     Você não pode se curar.')
            sleep(3)

      def raio_de_gelo(self):
            custo = 30
            if self.energia >= custo:
                  self.energia -= custo
                  laplace.vida -= 25
                  print('     -')
                  print('     Laplace foi congelado por um momento!')
                  print('     Laplace perdeu 25 de vida.')
            else:
                  print('     O jogador não tem energia o suficiente.')
                  print('     Você está cansado.')
            sleep(2)

      def bola_de_fogo(self):
            custo = 80
            if self.energia >= custo:
                  self.energia -= custo
                  laplace.vida -= 45
                  print('     -')
                  print('     Laplace foi atingido por uma bola de fogo!')
                  print('     Laplace perdeu 45 de vida.')
            else:
                  print('     O jogador não tem energia o suficiente.')
                  print('     Você está cansado.')
            sleep(2)
      
      

class enemy(Entidade):
      def __init__(self):
            super().__init__(vida=200, energia=100)

jogador = player()
laplace = enemy()