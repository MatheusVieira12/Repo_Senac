inicio = float(input("Digite o valor do odômetro no início do dia (km): "))
fim = float(input("Digite o valor do odômetro no fim do dia (km): "))
litros_consumidos = float(input("Digite a quantidade de combustível consumida (litros): "))
valor_recebido = float(input("Digite o valor total recebido dos passageiros (R$): "))

preco_combustivel = 4.87
distancia = fim - inicio
media_consumo = distancia / litros_consumidos
gasto_combustivel = litros_consumidos * preco_combustivel
lucro_liquido = valor_recebido - gasto_combustivel

print("\n--- RELATÓRIO DO DIA ---")
print("Distância percorrida:", distancia, "km")
print("Média de consumo:", round(media_consumo, 2), "km/l")
print("Gasto com combustível: R$", round(gasto_combustivel, 2))
print("Lucro líquido do dia: R$", round(lucro_liquido, 2))
