#Calcular area para saber quantas latas de tinta são necessárias para pintar

largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))

area = largura * altura
quantidade: float = area / 2

print('Quantidade necessária de tinta: {:.2f} litros'.format(quantidade))

