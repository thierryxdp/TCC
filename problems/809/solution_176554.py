def intercala(lista1, lista2):
    """A função intercala entre os elementos da lista 1 e lista 2
    lista, lista -> lista"""
    
    lista3 = lista1[1:1] + [lista2[0]]
    lista3 = lista1[3:3] + [lista2[1]]
    lista3 = lista1[5:5] + [lista2[2]]
    
    return lista3