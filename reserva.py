while True:
    try:
        nome = input('digite seu nome: ').title()
        break
    except:
        print('entrada errada, digite novamente.')

while True:
    try:
        noite = int(input('digite quantos noites irá se hospedar: '))
        break
    except:
        print('entrada errada, digite novamente.')

while True:
    try:
        quarto = input('digite o tipo de quarto (genin, jounin, hokage): ')
        break
    except:
        print('entrada errada, digite novamente.')

genin = 120 * noite
jounin = 180 * noite
hokage = 250 * noite

if quarto == 'genin':
    print(f'olá {nome}, o total da sua estadia é {genin}')
elif quarto == 'jounin':
    print(f'olá {nome}, o total da sua estadia é {jounin}')
elif quarto == 'hokage':
    print(f'olá {nome}, o total da sua estadia é {hokage}')