def eh_quadrada (m: list)-> bool:
    '''Retorna 'True' caso m seja uma matriz quadrada e 'False' caso contrário'''
    for lista in m:
        if len(m) == len(lista):
            return True
        else:
            return False