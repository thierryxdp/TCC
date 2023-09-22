def intercala(lista1, lista2):
    """Retorna uma lista que intercala os elementos das listas 1 e 2, dadas como entrada"""
    a=lista1
    b=lista2
    return [a[0]]+[b[0]]+[a[1]]+[b[1]]+[a[2]]+[b[2]]