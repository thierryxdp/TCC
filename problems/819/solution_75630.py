def filtraMultiplos(list_n1,n):
    '''Função que dado um numero, retorna o numero de multiplos correspondentes daquele numero.
    list,float -> list'''
    i=0
    list_n2=[]
    while i<len(list_n1):
        if list_n1[i] % n = 0:
            list_n2=list_n2+[list_n1[i]]
    return list_n2