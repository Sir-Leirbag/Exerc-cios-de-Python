#Organizando seu portfólio

projetos = ['Website', 'Jogo', 'Análise de dados', None, 'Aplicativo móvel']

for projeto in projetos:
    if projeto == None:
        print('- Projeto ausente')
        continue
    print(f'- {projeto}')
