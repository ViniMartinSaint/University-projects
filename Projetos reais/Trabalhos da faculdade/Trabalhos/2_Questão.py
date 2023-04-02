# O "total_pedido" antes do while serve para ocupar o valor do produto escolhido, assim efetuando a soma
# total do pedido sem problema. 
total_pedido = 0
while True:
    print("Bem-vindo a lanchonete do Vinicius Martins dos Santos, a melhor de Belford Roxo!!!")
    print("**************Cardápio***************")
    print("| Código |       Descrição        |  Valor   |")
    print("|  100   |    Cachorro Quente     | R$  9,00 |")
    print("|  101   | Cachorro Quente Duplo  | R$ 11,00 |")
    print("|  102   |        X-Egg           | R$ 12,00 |")
    print("|  103   |       X-Salada         | R$ 12,00 |")
    print("|  104   |        X-Bacon         | R$ 14,00 |")
    print("|  105   |        X-Tudo          | R$ 17,00 |")
    print("|  200   |   Refrigerante Lata    | R$  5,00 |")
    print("|  201   |      Chá gelado        | R$  4,00 |")

    # Parte que ocorrerá a repetição para determinar se a opção é inválida ou não
    while True:
        produto_escolhido = int(input("Digite o código do produto desejado: "))
        opt_valida = (produto_escolhido >= 100 and produto_escolhido < 106) or (produto_escolhido >= 200 and produto_escolhido < 202)
        if opt_valida: 
            break
        else:
            print("Opção inválida!")
            continue
            
    # Todas as codições baseadas no código escolhido pelo cliente
    valor_pedido = 0

    if (produto_escolhido == 100 ):
        produto = "Cachorro Quente"
        valor_pedido = 9.00
        total_pedido = total_pedido + valor_pedido
        print("Você pediu um {} no valor de R$ {:.2f} ".format(produto,valor_pedido))
        
    elif (produto_escolhido == 101 ):  
        produto = "Cachorro Quente Duplo"
        valor_pedido = 11.00
        total_pedido = total_pedido + valor_pedido

        print("Você pediu um {} Duplo no valor de R$ {:.2f}".format(produto,valor_pedido))

    elif (produto_escolhido == 102 ):
        produto =  "X-Egg"
        valor_pedido = 12.00
        total_pedido = total_pedido + valor_pedido
        print("Você pediu um X-Egg no valor de R$ 12,00 ".format(produto,valor_pedido))

    elif (produto_escolhido == 103 ):
        produto = "X-salada"
        valor_pedido = 12.00
        total_pedido = total_pedido + valor_pedido
        print("Você pediu um {} no valor de R$ {:.2f}".format(produto,valor_pedido))  

    elif (produto_escolhido == 104 ): 
        produto = "X-Bacon"
        valor_pedido = 14.00
        total_pedido = total_pedido + valor_pedido
        print("Você pediu um {} no valor de R$ {:.2f}".format(produto,valor_pedido))

    elif (produto_escolhido == 105 ):  
        produto = "X-Tudo"
        valor_pedido = 17.00
        total_pedido = total_pedido + valor_pedido
        print("Você pediu um {} no valor de R$ {:.2f}".format(produto,valor_pedido))

    elif (produto_escolhido == 200 ):  
        produto = "Refrigerante Lata"
        valor_pedido = 5.00
        total_pedido = total_pedido + valor_pedido
        print("Você pediu um {} no valor de R$ {:.2f}".format(produto,valor_pedido))

    else:
        produto = "chá gelado"
        valor_pedido = 4.00
        total_pedido = total_pedido + valor_pedido
        print("Você pediu um {} no valor de R$ {:.2f}".format(produto,valor_pedido))

    # Perguntar para cliente se ele deseja outro produto
    novo_pedido = int(input("Deseja pedir mais alguma coisa?\n 1 - sim \n 0 - não\n>>"))
    if novo_pedido != 1:
        break

# O total do pedido quando o cliente não deseja mais nenhum produto (Saindo do loop de cima)
print("Total do pedido: R$ {:.2f}".format(total_pedido))