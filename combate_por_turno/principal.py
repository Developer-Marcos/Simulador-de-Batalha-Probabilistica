from personagens import *
from acoes import *
from os import system 

system("cls")

explicacao()

print("Deseja começar o jogo?")

comecar = input("Responda (S/N): ").lower()
while True:
      if comecar in ('nao','n'):
            print('Tudo bem, caso mude de idéia é só executar o arquivo novamente.')
            sleep(1)
            exit()
      elif comecar not in ('sim', 's'):
            print('Digite apenas sim ou não.')
            comecar = input('Responda (S/N): ')
      else:
            break
sleep(1)
system("cls")
print('Laplace está ansioso para enfrenta-lo.')
print('Boa sorte.')
sleep(3)

start = True if comecar in ("sim", "s") else False
if not start:
      sair()

turno = 0
while start:
      if jogador.estar_vivo() and laplace.estar_vivo():
            system("cls")
            turno += 1
            status()
            print(f"     Turno: {turno}")
            print("     --------")
            escolher()
      elif jogador.estar_vivo():
            system('cls')
            print("     Laplace foi derrotado com sucesso!")
            print("     O sistema agradece ao jogador.\n")
            sair()
      else:
            system('cls')
            print("     O jogador foi derrotado!")
            print("     Você foi morto por Laplace.")
            sair()