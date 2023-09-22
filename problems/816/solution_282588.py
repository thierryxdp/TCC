def maiores(lista, n):
    """
    Dada uma lista de números e um número n, retorna uma outra lista contendo os números maiores do que n
    e os inserem dentro dessa nova lista.
    list, str -> list
    """
    list(lista)
    lista.append(n)
    listaOrganizada = sorted(lista)
    indicen = listaOrganizada.index(n)
    
    if n not in listaOrganizada:
        lista.append(n)
        
        return listaOrganizada[indicen + 1:]