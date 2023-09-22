#Start your python function here
def par(x):
    """Verifica se um número é ou não par"""
    if x%2==0:
        return True
    else:
        return False
def filtra_pares(a,b,c,d):
    t=(a,b,c,d)
    t=list(t)
    n=filter(par,t)
    return tuple(n)