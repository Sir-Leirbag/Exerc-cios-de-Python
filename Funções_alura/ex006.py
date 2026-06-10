numeros = input('Digite os números separados por espaço: ').split()
lista = list(map(int, numeros))

pares = list(filter(lambda x: x % 2 == 0, lista))

print(f'Os números pares são: {list(pares)}')
print('Os números pares são: ', ' '.join(str(pares)))
