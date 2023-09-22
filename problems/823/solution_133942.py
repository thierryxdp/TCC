def faltante(lista):
    """dada uma lista, retorna os elementos que faltam. int->int"""
    pecas=len(lista)
    lista.sort()
    i=0
    while i<pecas:
        if lista[i]]!=i+1:
            return i+1
        i=i+1
    return i+1