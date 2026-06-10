def calcular_idade(ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = calcular_idade(ano_atual, ano_nascimento)

print(f'A idade é {(idade)} anos.')
