
cliente = []
while True:
    try:
        produto = (input('Digite quantos produtos quer adicionar: '))
        cliente.append(produto)
        sair = input('Deseja inserir mais um produto: (S/N)').upper().strip()
        if sair == 'N':
            break

    except:
        print('Digite um numero valido: ')

print(cliente)