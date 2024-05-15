itensA = ["girafa", "abacaxi", "elefante", "banana", "macaco"]

def acharIndice(lista, elemento):
    for i in range(len(lista)):
        if elemento == lista[i]:
            print(f'o elemento selecionado está no indice {i}')
            return i
    return False

indice = acharIndice(itensA, 'ai')
print(indice)
