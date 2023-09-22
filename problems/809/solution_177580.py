def intercala(lista1, lista2):
    """Função que dada duas listas de tamanho 3 gera uma terceira lista
       que intercala os elementos da primeira lista e da segunda lista
       list, list ->list"""
    lista3 = lista1 + lista2
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3