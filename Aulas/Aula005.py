#Nessa aula aprendemos Manipulação de Strings/Texto

#Manipulação de strings em Python

#Concatenar '+', juntar/somar strings
# Útil quando você precisa combinar várias partes de texto em uma única mensagem
string1 = "Olá"
string2 = 'Mundo'
resul = string1 + " " + string2
print('CONCATENAR/SOMAR STRINGS "+" ')
print(resul)
print('\n')
#dá erro se tentar somar número

# Repetir/multiplicar uma string '*'
# Útil em situações como criar linhas de separação em um texto ou gerar padrões repetitivos, para não precisar criar loops adicionais
resul2 = string1 * 3
print('REPETIR/MULTIPLICAR UMA STRING "*"')
print(resul2)
print('\n')
# erro se tentar multiplicar por um valor não inteiro

# verificar se há um substring dentro de uma string maior 'in'
print('VERIFICAR SE HÁ PALAVRA DENTRO DA STRING "in"')
string3 = 'O astronauta finalmente conseguiu pousar em Marte e fincar a bandeira de seu país.Ao se virar para a câmera, percebeu que havia alguém acenando para ele da janela de um restaurante.A placa do estabelecimento dizia: "Aberto 24 horas".'
resul3  = 'virar' in string3.lower()
print(resul3)
print('\n')
#erro comum, in é sensível a letras MAI e MINUS. Para evitar, converter tudo para MINUS antes de verificar.

#Funções do Python para strings

#Transformando em STRING 'str'
# útil para garantir que um valor seja tratado como texto, independentemente de seu tipo original.
print('TRANSFORMAR QUALQUER TIPO PARA STRING, SERÁ TRATADO COMO STRING "str"')
n1 = 58
string4 = 'O número é: ' + str(n1)
print(string4)
print('\n')
# Essencial para a conversão de diferentes tipos de dados em strings, especialmente ao trabalhar com entradas de usuário ou dados de arquivos.

#Verificar tamanho da STRING 'len'
#Útil para várias operações que dependem do tamanho de uma string, como validação de senha ou formatação de texto.
print('TAMANHO DA STRING "len"')
tamanho = len(string3)
print(f'O número tem {tamanho} caracteres')
print('\n')
#Tentar aplicar len() a tipos de dados que não são sequências resultará em erro, verificar se o valor passado é uma string ou sequência

#Indexação de strings em Python
# Permite acessar e manipular partes específicas de uma string.

#Retornando um caractere da string '[]'
#Lembre-se de que a indexação começa em 0

string5 = 'Ola Mundo'
print('RETORNA ÍNDICE DO CARACTERE DESEJADO "[]" ')
print(string5[0])
print(string5[1])
print(string5[2])
print('\n')

#Slicing de strings
print('Permite acessar uma subsequência de caracteres usando a notação s[início:fim]')
print(string5[1:3])
print(string3[1:12])
print('\n')

#Slicing com índices negativos
print('Permite acessar elementos a partir do final da string')
print(string5[-7:-1])
print('\n')


#Invertendo uma string em Pythonp
print('Invertendo uma string: pode ser feito com slicing e passo negativo')
print(string5[::-1])
print('\n')

#Métodos de strings em Python

# Transforma primeira letra maiúscula com .capitalize()
print('Transforma primeira letra em maiúscula')
string6 = 'python is INCRÍVEL!'
print(string6.capitalize())
print('\n')

#Primeira letra maiúscula com .title()
#coloca a primeira letra de cada palavra em maiúscula
print('Primeira letra maiúscula com .title()')
print(string6.title())
print('\n')

#Invertendo a capitalização com .swapcase()
print('Inverte a capitalização de cada letra na string: De MAI para MINUS e vice versa')
print(string6.swapcase())
print('\n')

#Texto em maiúsculo com .upper()
print('Converte todos os caracteres de uma string para maiúsculas')
print(string6.upper())
print('\n')

#Texto em minúsculo com .lower()
print('Converte todos os caracteres de uma string para minúsculas')
print(string6.lower())
print('\n')

#Contando substrings com .count()
print('Conta o numero de substrings daquela string')
string7 = "Hoje em dia todo dia é um novo dia. Mais um dia chega. Dia!"
print(string7.count('dia'))
print('\n')

#Verificando final de uma string com .endswith()
print('Verifica se uma string termina com uma determinada substring:')
print(string7.endswith('!'))
print('\n')

#Verificando início de uma string com .startswith()
print('Verifica se uma string começa com uma determinada substring:')
print(string7.startswith('Hoje'))
print('\n')

#Buscando uma substring com .find()
print('Retorna o índice da primeira ocorrência de uma substring dentro de uma string. Se não for encontrada, retorna -1:')
print(string7.find('Hoje'))
#Pode dar erro se a palavra for escrita com MINUS e na string está em MAIS
print('\n')

#Substituindo caracteres com .replace()
print('Substitui todas as ocorrências de uma substring por outra:')
string8 = 'Eu gosto de maçã'
resul4 = string8.replace('maçã','maracúja')
print(resul4)
print('\n')

#Removendo espaços em branco com .strip()
print('Remove espaços em branco do início e do fim de uma string:')
string9 = '         Eu me chamo Ana  '
print(string9.strip())
print('\n')

#Encontrando index com .index()
print('Retorna o índice da primeira ocorrência de uma substring dentro de uma string, mas gera erro se não for encontrada:')
print(string9.index('me'))
print('\n')

#Identificação de caracteres de strings

#str.isalnum()
print('Verifica se todos os caracteres de uma string são alfanuméricos')
print(string9.isalnum())
print('\n')

#str.isalpha()
print('Verifica se todos os caracteres de uma string são letras:')
print(string9.isalpha())
print('\n')

#str.isdigit()
print('Verifica se todos os caracteres de uma string são dígitos:')
print(string9.isdigit())
print('\n')

#str.islower()
print('Verifica se todos os caracteres alfabéticos de uma string estão em minúsculas:')
print(string9.islower())
print('\n')

#str.istitle()
print('Verifica se a string está no formato de título, ou seja, se cada palavra começa com uma letra maiúscula seguida de letras minúsculas.')
print(string9.istitle())
print('\n')
