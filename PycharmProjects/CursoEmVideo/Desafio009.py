#Calcular aumento de salário

salario = float(input('Qual o seu salario atual: '))
aumento: float = salario*0.15 + salario

print('O salário atual com aumento de 15% fica em: {:.2f}'.format(aumento))