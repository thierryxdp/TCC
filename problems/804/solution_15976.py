#Start your python function here
def par(x):
    """Verifica se um número é ou não par"""
    if x%2==0:
        return True
    else:
        return False
def filtr(a,b,c,d):
    n=a,b,c,d
    list(filter(par,n))=h
    n=tuple(h)
    return n