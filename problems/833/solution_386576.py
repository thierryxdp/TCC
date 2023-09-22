def conta_numero(numero, matriz):
    ''' função que calcula os números dado um inteiro e uma matiz de tamanho qualquer Retorna quantas vezes esse número aparece na matriz'''
    '''int,list->int'''
    quantidade=0
    for n in matriz:
        for i in n:
            if i == numero:
                quantidade+=1
    return quantidade