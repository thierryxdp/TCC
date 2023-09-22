def eh_quadrada(lista):
    if len(lista)==0:
        return True
    elif len(lista) == len(lista[0]):
        return True
    else:
        return False