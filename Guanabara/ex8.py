#Conversor de Medidas

distancia = float(input('Uma distância em metros: '))

print(f'A medida de {distancia}m corresponde a:')
print(f'{distancia/1000}km')
print(f'{distancia/100}hm')
print(f'{distancia/10}dam')
print(f'{distancia*10:.0f}dm')
print(f'{distancia*100:.0f}cm')
print(f'{distancia*1000:.0f}mm\n')
