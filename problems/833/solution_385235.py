def conta_numero(numero, matriz):
    '''Coloque um numero e uma matriz e o resultado erá a quantidade de vezes que esse número aparece na matriz'''
    num=0
    for i in matriz:
        for aij in i:
            if aij==numero:
                num=num+1
    return num