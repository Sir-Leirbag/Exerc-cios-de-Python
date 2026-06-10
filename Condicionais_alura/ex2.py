#Calculando o tempo total de projeto

atividade_a = int(input('Informe os dias para a atividade A: '))
atividade_b = int(input('Informe os dias para a atividade B: '))
atividade_c = int(input('Informe os dias para a atividade C: '))

total_de_dias = atividade_a + atividade_b + atividade_c

if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
    print('Erro: os dias não podem ser negativos.')
else:
    print(f'O número total de dias é: {total_de_dias} dias')