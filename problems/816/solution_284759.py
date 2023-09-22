from math import*
def maiores(lista,numero):
    """Função que dada uma lista de números interios
    e um numero inteiro n, retorna outra lista, que contenha
    os numeros da lista original maiores que n.
    list,int -> list"""
    list.append(lista,numero)
    list.sort(lista)
    x=list.index(lista,numero)
    return lista[x:]