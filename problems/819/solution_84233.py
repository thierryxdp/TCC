def filtraMultiplos(lista,n):
    '''Retorna uma lista contendo os múltiplos de 'n'.
    Assinatura: list,int->list'''
    mult=[]
    for x in lista:
        if x% n==0:
            mult.append(x)
    return mult