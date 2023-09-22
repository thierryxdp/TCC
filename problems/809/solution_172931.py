"""Considerando que foi explicitado que as listas só possuem 3 componentes, então
a função irá intercalar os elementos da lista 1 com os da 2; com a observação de que 
há o limite de 3 componentes"""

def intercala(lista1,lista2):
    return [lista1[0], lista2[0], lista1 [1], lista2[1], lista1[2], lista2[2]]