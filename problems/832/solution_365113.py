def eh_quadrada(matriz):
    '''Retorna True se a matriz inserida é quadrada e False caso 
    contrário; list -> bool'''
    if matriz==[]:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False