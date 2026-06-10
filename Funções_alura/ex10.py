#função recursiva

n = int(input('Digite um número: '))

def calcular_soma (numero):
    if numero == 1:
        return 1
    else:
        return numero + calcular_soma(numero - 1)

print(f'A soma de 1 a {n} é: {calcular_soma(n)}')
