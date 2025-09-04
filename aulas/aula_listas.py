
produto = []
preço = []

while True:

    try:
        produto = (input('Digite o nome do produto: '))
        preço = int(input('Digite o preço do produto: '))
        op = int(input('quer adicionar mais um? '))
        if op == 'n':
            break

    except:
        print('Digite um numero valido: ')

print(cliente)