#Dissecando uma variável

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2

print(f'\nA soma vale: {s}')
print(f'A multiplicação vale: {m}', end = ' >>> ')
print(f'A divisão vale: {d:.2f}')
print(f'A divisão inteira vale: {di}')
print(f'A exponenciação vale: {e}')
print(f'O resto da divisão é: {r}\n')
