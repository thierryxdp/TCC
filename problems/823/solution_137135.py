def faltante(L):
    ''' list -> int'''
    x=1
    i=1
    while i <= len(L):
        if i in L :
            x=x
        else:
            x=i
        i+=1
    return x