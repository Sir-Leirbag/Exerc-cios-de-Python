#Contagem Regressiva

numero = 11

for i in range(1,numero):
    numero -= 1
    if numero % 2 == 0:
        print(f'Faltam apenas {numero} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {numero} segundos restantes.')
print('Aproveite a promoção agora!')
