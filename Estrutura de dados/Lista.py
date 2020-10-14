import copy

lista = [1,2,3,4,8,7,4,5]

#Add itens a uma lista
lista.append(1)

#Copiar uma lista já existente
lista_nova = copy.copy(lista)

#Contar quantas vezes determinado item aparece em uma lista
#Ex.: 1
print('Utilizando o count():',lista_nova.count(1))

#Adicionar um determinado item em uma determinada posição (posição,item)
lista_nova.insert(0,2000)
print('Utilizando o insert():',lista_nova)

#Reverter a ordem de uma lista
lista_nova.reverse()
print('Lista nova invertida:',lista_nova)

#Apagar determinado item que está contido na lista
lista_nova.remove(8)
print('Utilizando o remove():',lista_nova)

#Ordenando itens de uma lista
lista_nova.sort()
print('Utilizando o sort()  :',lista_nova)

#Remove o úlitmo item de uma lista
lista_nova.pop()
print('Utilizando o método pop():',lista_nova)

#Adicionando uma lista a outra
lista_nova.extend(lista)
print('Utilizando o método extend():',lista_nova)

#Mostra o indice do item especificado
print('Utilizando o método index():',lista_nova.index(1))

#Apaga toda a lista
lista_nova.clear()
print('Utilizando o método clear():',lista_nova)


