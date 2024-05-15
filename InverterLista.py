numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def inverterLista(lista):
    tamanho = len(lista) -1

                  #pega numero inteiro da divisão
    for i in range(len(lista)//2):
        aux = lista[i]
        lista[i] = lista[tamanho- i]
        lista[tamanho - i] = aux


inverterLista(numeros)
print(numeros)
