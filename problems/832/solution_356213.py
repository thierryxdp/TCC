def eh_quadrada(m):
    '''A função retorna True se a matriz for quadrada e False se a matriz não for quadrada;
    list[list,..]->bool'''
    if m==[]:
        return True
    elif len(m)==len(m[0]):
        return True
    else:
        return False