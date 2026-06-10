#Controle de acesso ao escritório

hora = int(input('Digite a hora atual (formato 24h): '))

if 8 <= hora < 18:
    print('Acesso concedido.')
else:
    print('Acesso negado.')
