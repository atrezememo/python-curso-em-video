#Converter metros em centimetros e milimetros

valorM = float(input('Digite um valor em metros: '))
centimetros = valorM*100
milimetros = valorM*1000

print('O valor em metros é {:.2f}\nEm centimetros {:.2f}\nEm milímetros {:.02f}'.format(valorM,centimetros,milimetros))
