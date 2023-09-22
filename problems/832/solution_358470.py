def eh_quadrada(lista):
    n_linha=(len(lista))
    n_col=(len(lista[0]))
    if lista==[]:
        return False
    elif n_linha==n_col:
        return True
    elif n_linha!=n_col:
        return False