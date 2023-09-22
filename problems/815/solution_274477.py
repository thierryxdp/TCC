""" Nesta função utilizamos 2 funções da própria lista, o append para adicionar
o elemento n e o sort para colocar a lista em ordem crescente.
"""
def insere(lista_numero, n):
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero