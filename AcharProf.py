professores = ['cordeiro', 'danilo', 'Lucas Silva', 'Lucas Augusto', 'Jones', 'Ana Claudia', 'Caio']
materias = ['SW', 'python', 'Front', 'Edge', 'Matematica', 'Story', 'Web']


for i in range(len(professores)):
    print(professores[i])

valido = False

while not valido:
    nome = input('Escolha um dos professores da lista acima:')

    for i in range(len(professores)):
        if professores[i] == nome:
            print(f'professor(a) {professores[i]}, dá a matéria {materias[i]}')
            valido = True
            break
