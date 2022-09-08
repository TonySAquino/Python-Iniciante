#ignorar drafts, apenas para rascunho

reprovado = 0
aprovado = 0
n = 0


while n == 0:
    nota = int(input('Digite a nota do aluno: '))
    if nota <6:
        reprovado = reprovado + 1
    else:
        aprovado = aprovado + 1
    n = int(input('Deseja continuar? se sim, digite 0, se não, digite qualquer outro numero: '))

print(f'{aprovado} alunos foram aprovados')
print(f'{reprovado} alunos foram reprovados')