def acharIndex(lista, elemento):
    elemento = elemento.lower()
    for i in range(len(lista)):
        if elemento == lista[i]:
            print(f'o elemento selecionado está no indice {i}')
            return i

def selecionarItem(lista, msg):
    for i in range(len(lista)):
        print(lista[i])

    escolha = input(msg)

    while not escolha in lista:
        escolha = input('Escolha um item valido: ')

    index = acharIndex(lista, escolha)
    print(f'voce escolheu o item {escolha} que é do ano {ano[index]} do valor {precos[index]}')
    return escolha

carros = ['up', 'uno', 'celtinha', 'gol', 'fusca']
precos = [10, 20, 100000, 15, 2]
ano = [2015, 2001, 2014, 2010, 1970]

selecionarItem(carros, 'Escolha o item da lista de carros: ')
