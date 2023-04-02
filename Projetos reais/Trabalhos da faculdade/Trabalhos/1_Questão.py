# Exigências:
# 1. Entre com o valor unitário do produto (Lembrar que número decimal é feito com ponto e não vírgula);
# 2. Entre com a quantidade desse produto;
# 3. O programa deve retornar o valor total sem desconto;
# 4. O programa deve retornar o valor total após o desconto
# 5. Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);
# 6. Colocar um exemplo de SAIDA DE CONSOLE de compra de mais de 10 und. (para mostrar que o desconto foi aplicado)

# Mensagem de boas vindas
print("Bem-vindo a Loja do Vinícius Martins dos Santos, O melhor atacado de Belford Roxo!") 

# Construção lógica do programa / Solicitação do programa
valor_produto = float(input("Digite o valor do produto: "))
qtd_produto = int(input("Digite a quantidade do produto: "))


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

total_sem_desconto = valor_produto * qtd_produto
total_com_desconto = total_sem_desconto - (total_sem_desconto * desconto)

# Resposta do programa / Output 
print('O valor total da compra sem desconto: R$ {:.2f}'.format(total_sem_desconto))
print('O valor total da compra com desconto: R$ {:.2f} ({} de desconto) '.format(total_com_desconto,desconto_formatado))
