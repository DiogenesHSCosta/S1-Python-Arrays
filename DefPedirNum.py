def checarNum(msg):

    numero = input(msg)

    while not numero.isnumeric():
        numero = input(msg)
    return numero

qtdGarrafas = checarNum('Diga a qtd de garrafas: ')
idade = checarNum('Diga sua idade: ')

print(f'sua idade é {idade} e pediu {qtdGarrafas} garrafas')
