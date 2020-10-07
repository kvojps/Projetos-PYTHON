import random
import string

letras = string.ascii_letters
numeros = '0123456789'
caracteres_especiais = '-+*%&!_'

total = letras + numeros + caracteres_especiais
tamanho = int(input("Digite o tamando da sua senha: "))

senha = ''.join(random.sample(total,tamanho))
print(senha)

