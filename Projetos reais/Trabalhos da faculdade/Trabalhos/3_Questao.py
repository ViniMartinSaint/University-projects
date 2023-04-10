# 3 de 4 exercicio da atividade prática

# Função de dimensão do pacote
def dimensoesObjeto():
    valor = 0
    while valor < 10:
        try:
            altura = float(input('Digite o valor da altura do objeto (em cm): '))
            comprimento = float(input('Digite o valor do comprimento do objeto (em Centimetros): '))
            largura = float(input('Digite o valor do largura do objeto (em Centimetros): '))
            volume = altura * comprimento * largura

            if volume < 1000:
                    valor = 10
            elif volume < 10000:
                    valor = 20
            elif volume < 30000:
                    valor = 30
            elif volume < 100000:
                    valor = 50
            else:
                print('O volume pacote de {} cm³'.format(volume))
                print("Dimensões do produto grandes demais.")
                print('Entre com as dimensões novamente')

        except ValueError:
                print("Digite um valor numérico inteiro, por gentileza!")

    print('O volume pacote de {} cm³'.format(volume))
    return valor
        
# Função do peso do objeto
def pesoObjeto():
    
    multiplicador = 0
    while multiplicador < 1 :
        try:
            peso = int(input('Digite o peso do objeto (em Kg): '))
            if peso <= 0.1:
                multiplicador = 1
            elif peso < 1:
                 multiplicador = 1.5
            elif peso < 10:
                multiplicador = 2
            elif peso < 30:
                multiplicador = 3
            else:
                print('Produto muito pesado para continuar a entrega! Escolha um objeto mais leve')
        
        except ValueError:
            print('Valor inválido! Digite um valor numérico')

    print('O multiplicador do pacote é de {}x'.format(multiplicador))        
    return multiplicador
    
# Função da rota do objeto
def rotaObjeto():
    print('RS - De Rio de Janeiro até São Paulo')
    print('SR - De São Paulo até Rio de Janeiro')
    print('BS - De Brasília até São Paulo')
    print('SB - De São Paulo até Brasília')
    print('BR - De Brasília até Rio de Janeiro')
    print('RB - Rio de Janeiro até Brasília')
    multiplicador = 0
    try: 
        while multiplicador < 1:
            rota = input("Digite a sigla da rota desejada (em maiúsculo): ")
            if rota == 'RS' or rota == 'SR':
                multiplicador = 1

            elif rota == 'BS' or rota == 'SB':
                multiplicador = 1.2

            elif rota == 'BR' or rota == 'RB':
                multiplicador = 1.5

            else:
                print('Digite um valor dentro da tabela, por favor')

        print('O multiplicador da rota é de {}x'.format(multiplicador))
        return multiplicador
    except ValueError:
        print('Digite somente uma string, valores numéricos não são válidos') 

# Todas as funções em funcionamento
print('Bem-vindo a companhia de logística Vinícius Martins dos Santos S.A.')
dimensao = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

# Calculo do total a pagar pelo transporte do pacote
total_a_pagar = dimensao * peso * rota
print('Total a pagar (R$): {} (Dimensões: {} * peso: {} * rota: {})'.format(total_a_pagar, dimensao, peso, rota))