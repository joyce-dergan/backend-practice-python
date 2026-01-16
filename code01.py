aluno = input('Nome do aluno:')
nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
nota3 = float(input('Nota 3:'))
nota4 = float(input('Nota 4:'))

media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
    print(f'Aluno {aluno} aprovado com média {media:.2f}')
else:
    print(f'Aluno {aluno} reprovado com média {media:.2f}')

# Fim do código
