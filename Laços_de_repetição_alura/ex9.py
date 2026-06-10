#Validação de entrada para login

#cadastro
while True:  
    nome = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    if len(nome) < 5:
        print('O nome de usuário deve conter pelo menos 5 caracteres.')
        continue
    if len(senha) < 8:
        print('A senha deve conter pelo menos 8 caracteres')
        continue
    print('Cadastro realizado com sucesso!')
    break
