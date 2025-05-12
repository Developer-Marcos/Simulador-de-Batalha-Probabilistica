from time import sleep
from random import choices, random, choice

class Entidade:
      def __init__(self, vida, energia):
            self.vida = vida
            self.energia = energia
      
      def estar_vivo(self):
            return self.vida > 0
          

class Player(Entidade):
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
            sleep(3)
      

      def meditar(self):
            valor = 40
            self.energia += valor if self.energia + valor < 100 else 100 - self.energia
            print('     -')
            print('     O jogador meditou.')
            print('     Recuperou +40 de energia.')
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
                  print('     +30 de vida para o jogador.')
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
            sleep(3)

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
            sleep(3)
      
      

class Enemy(Entidade):
      def __init__(self):
            super().__init__(vida=100, energia=100)

      def jogar(self):
            vida_jogador = jogador.vida
            energia_jogador = jogador.energia

            vida_laplace = laplace.vida
            energia_laplace = laplace.energia

            if vida_laplace > 35 and energia_laplace > 60:
                  if energia_jogador <= 20:
                        acoes = ['atacar', 'raio_maligno']
                        probabilidades = [0.7, 0.3]

                  elif energia_jogador >= 80:
                        if vida_jogador > 50:
                              acoes = ['ataque_caótico', 'raio_maligno', 'atacar']
                              probabilidades = [0.5, 0.3, 0.2]
                        else:
                              acoes = ['ataque_caótico', 'atacar']
                              probabilidades = [0.6, 0.4]

                  else:
                        if vida_jogador > 50:
                              acoes = ['atacar', 'raio_maligno', 'ataque_caótico', 'recarga']
                              probabilidades = [0.4, 0.3, 0.2, 0.1]
                        else:
                              acoes = ['atacar', 'raio_maligno', 'ataque_caótico', 'recarga']
                              probabilidades = [0.3, 0.2, 0.4, 0.1]

            elif vida_laplace <= 35 and energia_laplace > 60:
                  if vida_jogador > 50:
                              acoes = ['atacar', 'raio_maligno', 'ataque_caótico', 'recarga', 'regenerar']
                              probabilidades = [0.2, 0.1, 0.0, 0.2, 0.5]
                  else:
                              acoes = ['atacar', 'raio_maligno', 'ataque_caótico', 'recarga', 'regenerar']
                              probabilidades = [0.2, 0.2, 0.3, 0.1, 0.2]
            elif energia_laplace <= 60:
                  if vida_jogador > 50:
                        acoes = ['atacar', 'recarga']
                        probabilidades = [0.4, 0.6]
                  else:
                        acoes = ['atacar', 'recarga']
                        probabilidades = [0.3, 0.6]

            elif energia_laplace <= 30:
                  acoes = ['recarga']
                  probabilidades = [1.0]


            escolha = choices(acoes, weights=probabilidades)[0]

            if escolha == 'atacar':
                  prob = random()
                  if prob >= 0.25:
                        self.atacar()
                  else:
                        print('     -')
                        print('     Laplace errou o ataque!')
                        print('     -')
                        sleep(3)
            elif escolha == 'raio_maligno':
                  prob = random()
                  if prob >= 0.35:
                        self.raio_maligno()
                  else:
                        print('     -')
                        print('     Laplace tentou conjurar o Raio Maligno, mas falhou!')
                        print('     -')
                        sleep(3)
            elif escolha == 'ataque_caótico':
                  prob = random()
                  if prob >= 0.6:
                        self.ataque_caotico()
                  else:
                        print('     -')
                        print('     O Ataque Caótico de Laplace colapsou antes de atingir!')
                        print('     -')
                        sleep(3)
            elif escolha == 'regenerar':
                  self.regenerar()
            elif escolha == 'recarga':
                  self.recarga()
            
      def atacar(self):
            custo = 20
            if self.energia >= custo:
                  laplace.vida -= 15
                  self.energia -= custo
                  print('     -')
                  print('     Laplace atacou o jogador!')
                  print('     Você perdeu 15 de vida.')
                  print('     -20 de energia para laplace.')
            else:
                  print('     Laplace não tem energia o suficiente.')
                  print('     Ele precisa descansar.')
            sleep(3)

      def regenerar(self):
            valor = 30
            custo = 30
            if self.energia >= custo:
                  self.vida += valor if self.vida + valor < 100 else 100 - self.vida
                  self.energia -= custo
                  print('     -')
                  print('     Laplace se regenerou.')
                  print('     +30 de vida para Laplace')
            else:
                  print('     Laplace não tem energia o suficiente.')
                  print('     Ele precisa descansar.')
            sleep(3)

      def recarga(self):
            valor = 40
            self.energia += valor if self.energia + valor < 100 else 100 - self.energia
            print('     -')
            print('     Laplace regenerou a própria energia.')
            print('     +40 de energia para Laplace.')
            sleep(3)

      def raio_maligno(self):
            custo = 30
            if self.energia >= custo:
                  self.energia -= custo
                  jogador.vida -= 25
                  print('     -')
                  print('     Laplace atirou um raio maligno!')
                  print('     O jogador perdeu 25 de vida.')
            else:
                  print('     Laplace não tem energia o suficiente.')
                  print('     Ele precisa descansar.')
            sleep(3)
      
      def ataque_caotico(self):
            custo = 80
            if self.energia >= custo:
                  self.energia -= custo
                  jogador.vida -= 35
                  print('     -')
                  print('     Laplace distorce ass leis da fisica!')
                  print('     Jogador perdeu 35 de vida.')
            else:
                  print('     O Laplace não tem energia o suficiente.')
                  print('     Ele precisa descansar.')
            sleep(2)
      
      def falar(self):
            frases = [
                  "Você não vai sair vivo daqui.",
                  "Está cansado? Ainda nem comecei.",
                  "Seu fim é inevitável.",
                  "Você é só um erro no sistema.",
                  "Interessante... você ainda tenta lutar.",
                  "O caos é a única constante.",
                  "Não lute contra o inevitável.",
                  "Cada movimento seu é previsível.",
                  "Eu calculei sua morte antes de você pensar em me enfrentar.",
                  "Seus esforços são... estatisticamente irrelevantes.",
                  "A entropia sempre vence no final.",
                  "Dor é apenas um dado irrelevante.",
                  "Por que você insiste em resistir?",
                  "Você não entende as forças com que está lidando.",
                  "A ordem não pertence a este mundo.",
                  "Observe enquanto tudo se desfaz.",
                  "Laplace vê tudo. Laplace prevê tudo.",
                  "Isso não é um jogo. É o colapso do seu destino.",
                  "Se eu fosse humano, talvez sentisse pena.",
                  "Você já perdeu. Só não percebeu ainda.",
                  "A simulação chega ao fim.",
                  "O vazio é mais misericordioso que eu.",
                  "Você é o ruído. Eu sou o cálculo.",
                  "Continue. Quanto mais você luta, mais fraco se torna.",
                  "Isso é apenas uma repetição de sua derrota."
            ]

            fala_escolhida = choice(frases)

            print(f'Laplace diz: {fala_escolhida} ')


jogador = Player()
laplace = Enemy()