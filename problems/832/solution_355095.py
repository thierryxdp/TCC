def eh_quadrada(m):
    '''retorna True se a matriz for quadrada e False se não for quadrada
    list->bool'''
    if len(m)==len(m[0]) or m=[]:
        return True
    else:
        return False