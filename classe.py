import os
from salvler import *
from random import randint

class veículos():

    def cadveiculo() :
        veículos = {}
        veículos['Placa'] = randint(100,1000)
        veículos['Marca'] = (input('Digite a Marca do Veículo: '))
        veículos['Modelo'] = (input('Digite o Modelo do Veículo: '))
        veículos['Ano'] = int(input('Digite o Ano do Veículo: '))
        veículos['Cor'] = (input('Digite a Cor do Veículo: '))
        veículos['Cambio'] = (input('Digite o tipo de o Câmbio: '))
        catag = lerJson()
        catag.append(veículos)
        gravarJson(catag)


    def alterar():
        catalogo = lerJson()
        print(25 * '-')
        placa = int(input('digite a Placa do veículo: '))
        print(25 * '-')
        while True:
            for i in catalogo:
                if placa == i['Placa']:
                    placa = i['Placa']
                    marcas = i['Marca']
                    modelos = i['Modelo']
                    ano = i['Ano']
                    cor = i['Cor']
                    cambio = i['Cambio']
                    print(f'A Placa do Veículo é: {placa}')
                    print(f'A Marca Do Veículo é: {marcas}')
                    print(f'O Modelo do Veículo é: {modelos}')
                    print(f'O Ano do Veículo é: {ano}')
                    print(f'A Cor do Veículo é: {cor}')
                    print(f'O Câmbio do Veículo é: {cambio}')
                    print(25 * '-')
                    escolha = input('Digite qual Informação você deseja Alterar: ')
                    print(25 * '-')
                    escolha = escolha.upper()
                    if escolha == 'MARCA':
                        i['Marca'] = input('Digite a Nova Marca do Veículo: ')
                        print(25 * '-')
                    if escolha == 'MODELO':
                        i['Modelo'] = input('Digite o novo Modelo do Veículo: ')
                        print(25 * '-')
                    if escolha == 'ANO':
                        i['Ano'] = int(input('Digite o novo Ano do Veículo: '))
                        print(25 * '-')
                    if escolha == 'COR':
                        i['Cor'] = input('Digite a Nova Cor do Veículo: ')
                        print(25 * '-')
                    if escolha == 'CAMBIO':
                        i['Cambio'] = input('Digite o novo tipo de Câmbio do Veículo: ')
                        print(25 * '-')
                    if escolha == 'CÂMBIO':
                        i['Cambio'] = input('Digite o novo tipo de Câmbio do Veículo: ')
                        print(25 * '-')   
            gravarJson(catalogo)
            continuar = input('Deseja editar mais alguma Informação? S/N: ')
            continuar = continuar.upper()  
            if continuar == 'N':
                break


    def excluir():
        catalogo = lerJson()
        placa = int(input('digite a Placa do veículo: '))
        for i in catalogo:
            if i['Placa'] == placa:
                escolha = input('Deseja realmente deletar este veículo de nosso inventario? (S/N) ')
                escolha = escolha.upper()
                if escolha == 'S':
                    catalogo.pop()
                    print('O veículo foi excluido com sucesso.')
                gravarJson(catalogo)


    def consultar():
        catalogo = lerJson()
        for i in catalogo:
            placa = i['Placa']
            marcas = i['Marca']
            modelos = i['Modelo']
            ano = i['Ano']
            cor = i['Cor']
            cambio = i['Cambio']
            print(f'A Placa do Veículo é: {placa}')
            print(f'A Marca Do Veículo é: {marcas}')
            print(f'O Modelo do Veículo é: {modelos}')
            print(f'O Ano do Veículo é: {ano}')
            print(f'A Cor do Veículo é: {cor}')
            print(f'O Câmbio do Veículo é: {cambio}')
            print(25 * '-')

    
    def opcoes():
        print('Essas são as nossas opções de filtro.')
        print('Atraves da Placa.')
        print('Atraves da Marca.')
        print('Atraves do Modelo.')
        print('Atraves do Ano.')
        print('Atraves da Cor.')
        print('Atraves do Câmbio.')
        print(25 * '-')
        filtro = input('Digite a opção de pesquisa: ')
        filtro = filtro.capitalize()
        if filtro == 'Ano':
            escolha = int(input('Digite o Ano que deseja filtrar: '))
        else:
            escolha = input('Digite oque deseja filtrar: ')
            escolha = escolha.capitalize()
        catalogo = lerJson()
        for i in catalogo:
            if i[filtro] == escolha:
                placa = i['Placa']
                marcas = i['Marca']
                modelos = i['Modelo']
                ano = i['Ano']
                cor = i['Cor']
                cambio = i['Cambio']
                print(f'A Placa do Veículo é: {placa}')
                print(f'A Marca Do Veículo é: {marcas}')
                print(f'O Modelo do Veículo é: {modelos}')
                print(f'O Ano do Veículo é: {ano}')
                print(f'A Cor do Veículo é: {cor}')
                print(f'O Câmbio do Veículo é: {cambio}')
                print(25 * '-')