def filtra_pares(x,y,z,w):
    '''a partir das entradas retorna apenas os elementos pares da solução'''
    tupla=[]
    if x%2==0:
        tupla.append(x)
    if y%2==0:
       	tupla.append(y)
    if z%2==0:
       	tupla.append(z)
    if w%2==0:
        tupla.append(w)
    return tupla