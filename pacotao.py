#Para este trabalho deverá ser desenvolvido um programa em python contendo os seguintes itens:

# Variáveis
# Entrada de dados utilizando a função input
# Condições com: if, elif ou else
# Repetições com: while ou for
# Uma forma de estrutura de dados: lista, tupla, dicionário ou conjunto
# Criar uma função (def) e utilizar no programa
# Deverá ser feita uma apresentação com slides contando um pouco do problema que deseja resolver e também demonstrar a utilização do programa para a turma. O trabalho deverá ser enviado também através do github (enviando o link do repositório).

#Data de entrega: 15/05/2024

#Deverá ser feito com até duas pessoas

#Vai ser um repositor de supermercado para os caras que colocam o estoque

while True:
    try:
        meu_dicionario = dict()
        menu = int(input('bem vindo ao programa de estoque de profuto\n 1 para adicionar, 2 para revisar, 3 para excluir, 0 para sair'))
        while menu == 1:
            
            produto = str(input("qual o nome do produto\n digite 0 pra sair"))
            if produto == '0':
                break
            valor = int(input("o avalor do produto"))
            meu_dicionario[produto] = valor
            print(meu_dicionario,)
            
            
        if menu == 2:
            print(meu_dicionario)
        else:
            True

        while menu == 3:
            print(meu_dicionario)
            produto = str(input('qual prooduto'))
            del meu_dicionario[produto]

        
        if menu == 0:
            print('obrigado por usar o programa')
            break
        

    except ValueError:
        print('por favor, digite apenas números')
    except TypeError:
        print('type errssos')   
    except NameError:
        print('name error')
    except:KeyError
    print('não encontrado')





