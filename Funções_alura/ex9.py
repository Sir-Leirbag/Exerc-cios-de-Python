desconto = int(input('Digite a porcentagem de desconto: '))
valor = float(input('Digite o valor da compra: '))

def criar_desconto (desconto):
    def preco_do_produto(valor):
        return valor - ((valor/100) * desconto)
    return preco_do_produto
    
desconto_aplicado = criar_desconto(desconto)
print(f'Preço final com desconto: {desconto_aplicado(valor)}')
