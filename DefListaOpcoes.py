itensA = ["girafa", "abacaxi", "elefante", "banana", "macaco"]
itensB = ["bicicleta", "abacate", "leão", "morango", "tigre"]

def selecionarItem(lista, msg):
    for i in range(len(lista)):
        print(lista[i])

    escolha = input(msg)

    while not escolha in lista:
        escolha = input('Escolha um item valido: ')

    print(f'voce escolheu o item {escolha}\n')
    return escolha


selecionarItem(itensA, 'Escolha o item da lista A: ')
selecionarItem(itensB, 'Escolha o item da lista B: ')
