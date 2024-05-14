carros = ['up', 'uno', 'celtinha', 'gol', 'fusca']
precos = [10, 20, 100000, 15, 2]
ano = [2015, 2001, 2014, 2010, 1970]

localMaior = 0
maior = precos[localMaior]

for i in range(len(precos)):
    if precos[i] > maior:
        maior = precos[i]
        localMaior=i

print(f'O carro mais caro é o {carros[localMaior]} e custa {precos[localMaior]} e foi fabricado em no ano{ano[localMaior]}')
