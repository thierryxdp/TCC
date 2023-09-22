def eh_quadrada(matriz):
    """ a seguinte função irá verificar se
    uma matriz é quadrada. list->bol"""
    
    if len(matriz)==0:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False