comprimento = float(input("Digite o comprimento da cozinha (m): "))
largura = float(input("Digite a largura da cozinha (m): "))
altura = float(input("Digite a altura da cozinha (m): "))

# Cálculo da área total das paredes
area_total = 2 * altura * (comprimento + largura)

# Cálculo das caixas (1 caixa cobre 1.5 m²)
caixas = area_total // 1.5


print("Área total das paredes:", area_total, "m²")
print("Quantidade de caixas necessárias:", round(caixas))