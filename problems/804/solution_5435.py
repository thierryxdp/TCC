def filtra_pares(a,b,c,d):
    '''Função que retorna uma nova tupla contendo apenas
    os elemetos pares da tupla original, na mesma ordem em que
    se encontravam.
    a=int,b=int,c=int,d=int->tuple'''
    x= a//2
    y= b//2
    z= c//2
    h= d//2
    return tuple(filtra_pares(x,y,z,h))