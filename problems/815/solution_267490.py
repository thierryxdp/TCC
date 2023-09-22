def insere(lista_numero,n):
    """Pede uma lista ordenada de números inteiros
    e um outro número inteiro n. Retorna uma nova lista
    ordenada com n na posição correta.
    list,int->list"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero