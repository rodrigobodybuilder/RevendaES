import os
from classe import *


def encerrar():
        parar = input('Caso Deseje Encerrar o Programa Digite x: ')
        print(25 * '-')
        parar = parar.upper()
        return parar
        

while True:
    os.system('cls')
    print(25 * '-')
    print('Bem Vindo a ES Veículos')
    print(25 * '-')
    print('1 - Cadastrar Veículos') 
    print('2 - Consultar Inventario')
    print('3 - Consultar por Filtro')
    print('4 - Alterar Inventario')
    print('5 - Excluir Veículo')
    print(25 * '-')

    escolha = int(input("Insira a opção desejada: "))
    if escolha == 1:
        veículos.cadveiculo()
        if encerrar() == 'X':
            break
    elif escolha == 2:
        veículos.consultar()
        print(25 * '-')
        
        if encerrar() == 'X':
            break
    elif escolha == 3:
        veículos.opcoes()
        
        if encerrar() == 'X':
            break
    elif escolha == 4:
        veículos.alterar()
        
        if encerrar() == 'X':
            break
    elif escolha == 5:
        veículos.excluir()
        
        if encerrar() == 'X':
            break