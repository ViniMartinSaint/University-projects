# Exercicio 04 de 04
# ------------- Início das variáveis Globais -------------
lista_produto = []
codigo_peca = 0 
# ------------- Fim das variáveis Globais -------------

# ------------- Inico das funções -------------

def cadastrarPeca(codigo):
    print('Você está no menu de Cadastrar Peça')
    print('Código da Peça: {}'.format(codigo))
    nome = input('Entre com o NOME da peça: ')
    fabricante = input('Entre com o FABRICANTE da peça: ')
    preco = float(input('Entre com o PREÇO(R$) da peça: '))
    dicionario_produto = {'código'     : codigo,
                          'nome'       : nome,
                          'fabricante' : fabricante,
                          'preço'      : preco}
    lista_produto.append(dicionario_produto.copy()) # Tem que fazer uma cópia dele para que a lista não seja atribuída ao dicionário    

def consultarPeca():
    while True:
        opcao_consultar = input('\nVocê está no menu de Consultar Peça (s):\n' +
                                    '1 - Consultar todas peças\n'+
                                    '2 - Consultar Peças por código\n' +
                                    '3 - Consultar Peças por Fabricante\n' +
                                    '4 - Retornar\n' +
                                    '>> ')
        if opcao_consultar == '1': # Todas as peças
            print('Você escolheu a opção Consultar Todas as peças')
            for peca in lista_produto: # peca vai consultar toda a lista de produtos
                print('-'*25)
                for key, value in peca.items():    
                    print('{}:{}'.format(key,value)) # Vai imprimir todos os dicionários que tem nessa lista
                print('-'*25)

        elif opcao_consultar == '2': # Código
            print('Você escolheu a opção Consultar Peças por código')
            valor_desejado = int(input('Entre com o CÓDIGO desejado: '))
            for peca in lista_produto:
                if peca['código'] == valor_desejado:
                    print('-'*25)
                    for key, value in peca.items():
                        print('{}: {}'.format(key,value))
                    print('-'*25)

        elif opcao_consultar == '3': # Fabricante
            print('Você escolheu a opção Consultar Peças por Fabricante')
            valor_desejado = input('Entre com o FABRICANTE desejado: ')
            for peca in lista_produto:
                if peca['fabricante'] == valor_desejado: # o valor do campo desse dicionário é igual o código desejado?
                        print('-'*25)
                        for key, value in peca.items():
                            print('{}:{}'.format(key,value)) # Vai imprimir todos os dicionários que tem nessa lista
                        print('-'*25)
            
        elif opcao_consultar == '4':
            return # Sai da função consultar_produto e volta para a Main
        
        else:
            print('Opção inválida, tente novamente.')
            continue # Volta para o início do laço

def removerPeca():
    print('Você está no menu de Remover Peça')
    valor_desejado = int(input('Entre com o CÓDIGO desejado: '))
    for peca in lista_produto:
        if peca['código'] == valor_desejado: # o valor do campo desse dicionário é igual o código desejado?
            lista_produto.remove(peca)
            print('Produto removido!')
# ------------- Fim das funções -------------

# ------------- Início de Main -------------
print('Bem-vindo ao controle de estoque da Bicicletaria do Vinícius Martins dos Santos')
while True:
    opcao_principal = input('\nEscolha a opção desejada:\n' +
                                '1 - Cadastrar peça\n'+
                                '2 - Consultar produto (s)\n' +
                                '3 - Remover produto\n' +
                                '4 - Sair\n' +
                                '>> ')
    if opcao_principal == '1':
        codigo_peca = codigo_peca + 1
        cadastrarPeca(codigo_peca)
    elif opcao_principal == '2':
        consultarPeca()
    elif opcao_principal == '3':
        removerPeca()
    elif opcao_principal == '4':
        print('Muito obrigado! Encerrando o programa...')
        break # Encerra o laço
    else:
        print('Opção inválida, tente novamente.')
        continue # Volta para o início do laço
# ------------- Fim da Main -------------
