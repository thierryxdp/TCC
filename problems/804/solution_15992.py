#Start your python function here
def par(x):
    """Verifica se um número é ou não par"""
    if x%2==0:
        return True
    else:
        return False
def filtrar_paress(a,b,c,d):
    t=(a,b,c,d)
    t=list(t)
    return tuple(filter(par,t))