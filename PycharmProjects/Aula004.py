import math
import random
import emoji
# aqui utilizamos o módulo de math que importa várias funções como, raiz quadrada, arredondamento etc.
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print ('O número escolhido foi {} e sua raiz quadrada é {:.2f}'.format(num, math.ceil(raiz)))

#Aqui utilizamos o módulo #random, que gera números aleatórios
num = random.randint(1,10)
print('O numero aleatório escolhido pelo programa foi {:.2f}'.format(math.ceil(num)))

#Também é possível instalar módulos criados por outros usuários que fica disponível na página do Python em "PyPi"
#Aqui vamos testar a emoji, que permite aparecer os emojis

print(emoji.emojize("Olá, mundo :beating_heart:",))