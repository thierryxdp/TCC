def repetidos(x):
    '''
    funcao retorna o numero de vezes que um elemento da lista x é repetido
    '''
    r=0
    i1=0
    i2=1
    while i2<len(x):
        if x[i1]==x[i2]:
            r=r+1
            i1=i1+1
            i2=i2+1
        elif x[i2]!=x[i1]:
            i1=i1+1
            i2=i2+1
    return r