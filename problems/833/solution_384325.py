def conta_numero(numero,matriz):
    '''
    '''
    i=0
    lista=[]
    while i<len(matriz):
        if numero in matriz[i]:
            lista.append(matriz[i].count(numero))
        i+=1
    return sum(lista)