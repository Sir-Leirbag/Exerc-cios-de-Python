#Controlando o orçamento mensal

despesas = float(input('Digite o total de despesas do mês(R$): '))

if despesas < 3000:
    print('O total de despesas está dentro do orçamento.')
else:
    print('Atenção! Você ultrapassou o limite do orçamento.')
