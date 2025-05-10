from combate_por_turno.personagens import *
from sys import exit
from time import sleep
from os import system

def sair():
      print("     Obrigado por jogar.\n")
      exit()

def explicacao():
      print("Olá jogador, seu objetivo é derrotar Laplace, o demônio da probabilidade.\n")

      print('A luta irá ocorrer por rodadas, onde cada entidade tem direito de jogar 1 vez por rodada.\n')

      print('A cada rodada será possivel executar ações.')
      print('Ações gastam energia.')
      print('O máximo de energia é 100.\n')

      print('O mesmo vale para Laplace.\n')

      print('A primeira rodada é sua, aproveite.\n')

def status():
      print(f"""
      __________________________________________________
           
      Sua vida:    {jogador.vida} | Vida de Laplace:    {laplace.vida}
      Sua energia: {jogador.energia} | Energia de Laplace: {laplace.energia} 
      __________________________________________________

      Escolha o que você irá fazer:
      [1] Atacar
      [2] Habilidades
      [3] Desistir
            """)
      
def habilidades_do_jogador():
      print(f"""  
            Escolha a habilidade:
            [1]  Meditação    ( Recupera no máximo 40 de energia )
            [2]  Regeneração  ( Regenera no máximo 30 de vida, -30 de energia )
            [3]  Raio de gelo ( Causa 25 de dano, -30 de energia )
            [4]  Bola de fogo ( Causa 60 de dano, -60 de energia)
            """)
      
      opc = input("            Sua opção de habilidade:  ")

      if opc == '1' and jogador.energia < 100:
            jogador.meditar()
      elif opc == '1' and jogador.energia >= 100:
            print('            -')
            print('            Sua energia já está no limite!')
            habilidades_do_jogador()
      elif opc == '2' and jogador.vida < 100:
            jogador.regenerar()
      elif opc == '2' and jogador.vida >= 100:
            print('            -')
            print('            Não é possível se curar além disso!')
            habilidades_do_jogador()
      elif opc == '3':
            jogador.raio_de_gelo()
      elif opc == '4':
            jogador.bola_de_fogo()
      else:
            print('            Essa opção é inválida.')
            print('            Não desperdice os seus turnos!')
            sleep(2)

def desistir():
      print("     -")
      opc = input('     Tem certeza que deseja desistir? [S/N]: ').lower()
      while True:
            if opc in ('sim','s'):
                  system("cls")
                  print('     Você desistiu.')
                  sair()
            elif opc not in ('nao', 'n'):
                  print('     Digite apenas sim ou não.')
                  opc = input('     Responda (S/N): ')
            else:
                  break

def escolher():
      opc = input('     Sua opção [1], [2] ou [3]: ')
      if opc == '1':
            jogador.atacar()
            
      elif opc == '2':
            habilidades_do_jogador()
      elif opc == '3':
            desistir()
      else:
            print('     Essa opção é inválida.')
            print('     Não desperdice os seus turnos!')
            sleep(2)
