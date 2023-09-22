#Start your python function here
def filtra_pares(t):
    """ Retorna uma tupla contendo elementos pares da tupla original que foi informada, na mesma ordem que foi encontrada """
    l=[]
    for n in t:
        if n%2==0:
            l.append(n)
            
    return tuple(l)