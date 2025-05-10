from combate_por_turno.personagens import *
from combate_por_turno.acoes import *
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
      if laplace.vida > 0:
            system("cls")
            turno += 1
            status()
            print(f"     Turno: {turno}")
            print("     --------")
            escolher()
      else:
            system('cls')
            print("     Laplave foi derrotado com sucesso!")
            print("     O sistema agradeceu ao jogador.\n")
            sair()