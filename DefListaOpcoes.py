itensA = ["girafa", "abacaxi", "elefante", "banana", "macaco"]
itensB = ["bicicleta", "abacate", "leão", "morango", "tigre"]

def selecionarItem(lista):
    for i in range(len(lista)):
        print(lista[i])

    escolha = input('Escolha um dos itens da lista: ')
    while not escolha in lista:
        escolha = input('Escolha um item valido: ')

    print(f'voce escolheu o item {escolha}')


selecionarItem(itensA)
selecionarItem(itensB)
