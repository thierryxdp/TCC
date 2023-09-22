def filtraMultiplos(x,y):
    '''Dada a lista X, retorna todos os números divisíveis por y
    list, float -> list.'''
    i=0
    while i<=len(x):
        if x[i]%y:
            list.append(x,x[i])
            i=i+1
        else:
            i=i+1
    return x