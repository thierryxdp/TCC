def repetidos(l):
    '''Calcula e retorna o número de vezes em que o número da lista l se repete em relação ao seu anterior.
    list-->int'''
    i1=0
    i2=1
    valor=0
    while i2<=len(l):
        if l[i1]==l[i2]:
            valor=valor+1
        i1=i1+1
        i2=i2+1
    return valor