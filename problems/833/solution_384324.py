def conta_numero(numero,matriz):
    '''
    '''
    i=0
    lista=[]
    while i<len(M):
        if numero in M[i]:
            lista.append(M[i].count(numero))
        i+=1
    return sum(lista)