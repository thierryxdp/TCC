def eh_quadrada(l):
    """dada uma lista matriz checa se a matriz é quadrada e retorna um valor booleano;
    list->bool"""
    if l==[]:
        return True
    elif len(l)== len(l[0]):
        return True
    else:
        return False