def faltante(l):
    '''Encontra a peça faltante.
    Assinatura:list->int'''
    i=0
    for x in l:
        if x-l[i-1]!=1 and i>0:
            return x-1
        else:
            if l[0]==2:
                return 1
        i=i+1
    return i+1