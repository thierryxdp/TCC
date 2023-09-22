def conta_numero(numero, matriz):
    '''dado um numero ele procura este mesmo numero na matriz
    e retona quantas vezes ele foi achado'''
    '''list->int'''
    a=[]
    for i in range (0,len(matriz)):
        for j in matriz[i]:
            if j==numero:
                a.append(j)
    return len(a)