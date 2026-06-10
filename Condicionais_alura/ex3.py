#Temperatura dos servidores

temperatura = float(input('Digite a temperatura do atual do ambiente: '))

if temperatura > 25:
    print('Alerta! Temperatura acima do limite permitido.')
else:
    print('Temperatura dentro do limite seguro.')