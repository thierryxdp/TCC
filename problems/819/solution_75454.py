def filtraMultiplos(l,n):
    '''
    Retorna todos os números da lista
    divisiveis pelo valor de n.
    list,int -> list
    '''
    x=0
    while x < len(l):
        if l[x]%n!=0:
            l.pop(x)
        else:
            x=x+1
    return l