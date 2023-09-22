def eh_quadrada(m):
    '''retorna True se a matriz for quadrada e False se não for quadrada
    list->bool'''
    if m==[]:
        return 
    elif len(m)==len(m[0]):
        return True
    else:
        return False