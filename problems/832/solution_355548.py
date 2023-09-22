def eh_quadrada(matriz):
    """Funcao booleana que diz se uma dada matriz é quadrada ou não;
    list->bool"""
    if len(matriz)==0:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False