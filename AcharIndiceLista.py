itensA = ["girafa", "abacaxi", "elefante", "banana", "macaco"]

def acharIndex(lista, elemento):
    elemento = elemento.lower()
    for i in range(len(lista)):
        if elemento == lista[i]:
            print(f'o elemento selecionado está no indice {i}')
            return i
    return False

indice = acharIndex(itensA, 'MACACO')
print(indice)
