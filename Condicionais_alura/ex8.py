#Calculando pedágio

distancia = int(input('Digite a distância percorrida (em KM): '))

if distancia <= 100:
    print('Valor do pedágio: R$ 10,00')
elif 100 < distancia <= 200:
    print('Valor do pedágio: R$ 20,00')
else:
    print('Valor do pedágio: R$ 30,00')
