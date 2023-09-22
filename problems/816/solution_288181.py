def maiores(lista, n):
    """ Função que dada uma lista de números e um número inteiro n retorna outra lista que contém numeros da lista maiores que n
    list,int -> list"""
    lista_final = []
for num in lista:
    if num > n:
    lista_final.append(num)
    print (lista_final)