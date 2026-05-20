#Calcular desconto em cima do preço do produto

preço = float(input('Qual o preço do produto: '))
preçoatual: float = preço*0.95
##Colocado 0.95 porque seria 95% do preço, já tirando os 5%, mais organizado do que
#subtrair
print('O preço atual com 5% de desconto é: {:.2f}'.format(preçoatual))

