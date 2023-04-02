
# Mensagem de boas vindas
print("Bem-vindo a Loja do Vinícius Martins dos Santos, O melhor atacado de Belford Roxo!") 

# Valores preenchidos pelo usuário do código / Preço do produto e quantidade dele
valor_produto = float(input("Digite o valor do produto: "))
qtd_produto = int(input("Digite a quantidade do produto: "))

# Condicionais baseadas na quantidades dos produtos
if (qtd_produto <= 9):
    desconto = 0
     
elif (10 <= qtd_produto <= 99):
    desconto = 0.05
    desconto_formatado = "5%"
elif (100 <= qtd_produto <= 999):
    desconto = 0.1
    desconto_formatado = "10%"
else:
    desconto = 0.15
    desconto_formatado = "15%"

# Formula final do cálculo da compra, seja com desconto ou sem
total_sem_desconto = valor_produto * qtd_produto
total_com_desconto = total_sem_desconto - (total_sem_desconto * desconto)

# Resposta do programa / Output 
print('O valor total da compra sem desconto: R$ {:.2f}'.format(total_sem_desconto))
print('O valor total da compra com desconto: R$ {:.2f} ({} de desconto) '.format(total_com_desconto,desconto_formatado))
