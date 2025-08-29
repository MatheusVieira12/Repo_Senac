
nome = input('digite o seu nome: ').title()

while True:
    try:
        nota1 = float(input('digite o numero1: '))
        break
    except:
        print('digite apenas numeros')

while True:
    try:
        nota2 = float(input('digite o numero2: '))
        break
    except:
        print('digite apenas numeros')

media = (nota1 + nota2)/2

if media < 5:
    print('reprovado')
elif media >= 5 and media < 8:
    print('recuperação')
else:
    print('aprovado')

print(f'O aluno {nome} ficou com a media:{media}')