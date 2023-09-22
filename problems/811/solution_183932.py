import math
def colchao(a,h,l):
    '''Retorna True para caso o colchao passe pela porta.
    Forneça as 3 medidas, em centímetros, do colchão em ordem crescente na lista e
    as dimensões da porta
    list, int, itn -> bool'''
    if a[1]<=h or a[1]<=l or a[2]<=h or a[2]<=l:
        return True
    else:
        return False