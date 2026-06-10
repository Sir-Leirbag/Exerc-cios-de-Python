#Tabuada

numero = int(input('Digite um número para ver sua tabuada: '))

print('-' * 12)
for i in range(1,11):
    print(f'{numero} x {i} = {numero * i}')
print('-' * 12)
