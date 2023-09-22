def conta_numero(numero, matriz):
    ''' função que calcula os números'''
    '''int,list->int'''
    quantidade=0
    for n in matriz:
        for i in n:
            if i == numero:
                qt+=1
    return quantidade