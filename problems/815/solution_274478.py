""" Nesta função utilizamos 2 funções da própria lista, o append para adicionar
o elemento n e o sort para colocar a lista em ordem crescente. Retornamos a 
própria lista, pois ao utilizar essas funções, o retorno é none, ou seja, as
alterações são feitas direto na lista, assim após aplicar as alterações apenas
retornamos a própria lista.
list, int -> list
"""
def insere(lista_numero, n):
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero