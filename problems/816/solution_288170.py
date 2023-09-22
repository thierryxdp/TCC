def maiores(lista, n):
    """ Função que dada uma lista de números e um número inteiro n retorna outra lista que contém numeros da lista maiores que n
    list,int -> list"""
    for numero in lista:
    if numero > n:
        lista.append(numero)
return lista