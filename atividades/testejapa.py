cardapio_japones = {
    "Temaki de salmão": 22.90,
    "Temaki califórnia": 20.90,
    "Temaki de atum": 23.90,
    "Temaki skin": 19.90,
    "Sashimi de salmão": 34.90,
    "Sashimi de atum": 36.90,
    "Sashimi de peixe branco": 32.90,
    "Uramaki califórnia": 24.90,
    "Uramaki salmão com cream cheese": 26.90,
    "Hossomaki de salmão": 18.90,
    "Hossomaki de kani kama": 17.90,
    "Hot roll": 28.90,
    "Gyoza": 21.90,
    "Yakisoba de carne": 29.90,
    "Yakisoba de frango": 27.90,
    "Missoshiru": 12.90,
    "Edamame": 14.90,
    "Sunomono": 11.90,
    "Donburi": 33.90,
    "Tempurá de legumes": 22.90
}


pedidos_registrados = []

def mostrar_cardapio():
    print("Cardápio Japonês:")
    for item, preco in cardapio_japones.items():
        print(f"{item}: R$ {preco:.2f}")

def registrar_pedido():
    while True:
        try:
            numero_mesa = int(input("Digite o número da mesa: "))
            break
        except:
            print("Número inválido. Tente novamente.")
    garcom = input("Digite o nome do garçom: ").capitalize()
    pedidos = []
    while True:
        pedido = input("Digite o nome do pedido (ou pressione Enter para finalizar): ").capitalize()
        if pedido == "":
            break
        if pedido not in cardapio_japones: # verifica se o pedido está no cardápio
            print("Pedido não encontrado no cardápio. Tente novamente.")
            continue
        pedidos.append(pedido) # adiciona o pedido à lista de pedidos
    numero_pedido = len(pedidos_registrados) + 1 # contador para que o número do pedido seja único, começa sem pedidos e vai adicionando 1 a cada novo pedido
    pedido_dict = {
        "numero_pedido": numero_pedido, 
        "mesa": numero_mesa,
        "garcom": garcom,
        "pedidos": pedidos
    }
    pedidos_registrados.append(pedido_dict)
    print(f"Pedido registrado com sucesso! Seu número do pedido é: {numero_pedido} ")

def fecharConta():
    while True:
        try:
            indice_pedido = int(input("Digite o número do pedido para fechar a conta: "))
            break
        except:
            print("Número inválido. Tente novamente.")
    for pedido in pedidos_registrados:
        if pedido["numero_pedido"] == indice_pedido: # verifica se o número do pedido existe
            total = sum(cardapio_japones[item] for item in pedido["pedidos"])
            print(f"Valor para o pedido de número {indice_pedido}: R$ {total:.2f}")
            return
        else:
            print("Pedido não encontrado.")

print('\n BEM VINDO AO MENU')
while True:
    try:
        op = int(input('\n Escolha uma opção: \n 1- Visualizar cardápio\n 2- Registrar pedido \n 3- Fechar a conta \n 4- Ver pedidos registrados \n 5- Sair \n'))
        if op not in [1, 2, 3, 4, 5]:
            print("Entrada inválida. Digite um número entre 1 e 5.")
            continue
    except:
        print("Entrada inválida. Digite um número entre 1 e 5.")
        continue

    match op:
        case 1:
            mostrar_cardapio()
        
        case 2:
            registrar_pedido()
        
        case 3:
            fecharConta()

        case 4:
            print(pedidos_registrados)
    
        case 5:
            print('Saindo do sistema...')
            break