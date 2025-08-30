potencia = int(input('digite a potência da lâmpada: '))
largura = float(input('digite a largura do cômodo: '))
comprimento = float(input('digite o comprimento do comôdo: '))
    
area = comprimento * largura
print(area)

#potencia total necessaria
potencia_total = potencia/area
if potencia < 3:
    print ('não é o ideal')
else:
    print(potencia_total)






