#Aprovando empréstimo

renda = float(input('Digite o valor da sua renda mensal: '))
parcela = float(input('Digite o valor da parcela desejada: '))
compromentimento_da_renda = (parcela/renda) * 100

if renda < 2000:
    print('Empréstimo negado: renda abaixo do valor mínimo.')
elif renda >= 2000 and compromentimento_da_renda <= 30:
    print('Empréstimo concedido.')
else:
    print('Empréstimo negado: parcela acima de 30% da renda.')
