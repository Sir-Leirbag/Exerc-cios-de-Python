primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
operacao = input('Escolha uma operação (| + | - | * | / |): ')

if operacao == '+':
    soma = lambda a, b: a + b
    print(f'O resultado é: {soma(primeiro_numero, segundo_numero)}')
elif operacao == '-':
    subtracao = lambda a, b: a - b
    print(f'O resultado é: {subtracao(primeiro_numero, segundo_numero)}')
elif operacao == '*':
    multiplicacao = lambda a, b: a * b
    print(f'O resultado é: {multiplicacao(primeiro_numero, segundo_numero)}')
elif operacao == '/':
    divisao = lambda a,b: a / b
    print(f'O resultado é: {divisao(primeiro_numero, segundo_numero)}')
else:
    print('Operação inválida.')