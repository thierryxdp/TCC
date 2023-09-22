def par(n):
    if n%2==0:
        return True
    else:
        return False
    
def filtra_pares(a,b,c,d):
    '''retorna os elementos pares da tupla original na mesma
    ordem em que se encontravem; int, int, int, int'''
    x=filtra_pares[:]
    return tuple(filter(par,x))