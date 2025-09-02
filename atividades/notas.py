nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
optativa = input("Deseja fazer a prova optativa? Digite -1 caso não tenha feito: ").lower()
if optativa != '-1':
    nota_optativa = float(input("Digite a nota da prova optativa: ")) 
    if nota1 < nota2 and nota_optativa > nota1:
        nota1 = nota_optativa
    elif nota2 <= nota1 and nota_optativa > nota2:
        nota2 = nota_optativa

media = (nota1 + nota2) / 2

print('\n-------Situação Final:--------')
print(f'Nota 1: {nota1}')
print(f'Nota 2: {nota2}')
print(f'Média: {media}')

if media >= 6:
    print('Aprovado!')
elif media >= 3 and media < 6:
    print('Exame')
else:
    print('Reprovado!')
