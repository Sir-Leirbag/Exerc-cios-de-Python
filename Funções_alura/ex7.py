produto = input('Digite os produtos separados por vírgula: ').split(',')
preco = input('Digite os preços separados por vírgula: ').split(',')

for produto, preco in zip(produto, preco):
    print(f'{produto.strip()}: {preco.strip()}')
