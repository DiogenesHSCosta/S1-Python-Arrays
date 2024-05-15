def maiorValor(lista):
    indice = 0
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            indice = i
            maior = lista[i]
    return indice


carros = ['up', 'uno', 'celtinha', 'gol', 'fusca']
precos = [10, 20, 100000, 15, 2]
ano = [2015, 2001, 2014, 2010, 1970]

maisCaro = maiorValor(precos)
print(maisCaro)
