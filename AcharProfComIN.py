professores = ['cordeiro', 'danilo', 'Lucas Silva', 'Lucas Augusto', 'Jones', 'Ana Claudia', 'Caio']
materias = ['SW', 'python', 'Front', 'Edge', 'Matematica', 'Story', 'Web']

nome = input('insira o nome de um prof')
            #in funciona como um for de busca
while not nome in professores:
    nome = input('insira o nome de um prof')

for i in range(len(professores)):
    if professores[i] == nome:
        print(f'{professores} dá {materias[i]}')
