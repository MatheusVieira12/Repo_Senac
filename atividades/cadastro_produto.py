nomes = []
valores = []


while True:
    try:
        quantidade_produto = int(input("Digite a quantidade do produto: "))
        break
    except:
        print("Entrada inválida. Tente novamente.")

for produto in range(quantidade_produto):
    while True:
        try:
            nome_produto = input("Digite o nome do produto: ").strip()
            break
        except:
            print("Erro ao cadastrar o produto.")
            
    while True:
        try:
            valor_produto = float(input("Digite o preço do produto: "))
            break
        except:
            print("Erro ao cadastrar o produto.")
            
    nomes.append(nome_produto)
    valores.append(valor_produto)
    print(f"Produto cadastrado: {nome_produto} - Preço: R${valor_produto:.2f}")


print('\n----Resumo do Cadastro de Produtos-----')
print(f'Nomes: {nomes}')
print(f'Valores: {valores}')