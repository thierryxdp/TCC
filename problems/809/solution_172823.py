def intercala(lista1, lista2):
    """Retorna uma terceira lista, que intercala os elementos da lista1 e lista2"""
    '''lista,lista -> lista'''
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]