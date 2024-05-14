def checarNum(msg, msgErro):

    numero = input(msg)

    while not numero.isnumeric():
        numero = input(msgErro)
    return numero

qtdGarrafas = checarNum('Diga a qtd de garrafas: ', 'Qtd de garrafas deve ser um numero: ')
idade = checarNum('Diga sua idade: ', 'idade deve ser um numero: ')

print(f'sua idade é {idade} e pediu {qtdGarrafas} garrafas')
