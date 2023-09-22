def conta_numero(numero,matriz):
    '''
    funcao recebe como entrada um numero e retorna quantas vezes ele está presente na matriz
    '''
    freq=0
    for conta in matriz:
        for el in conta:
            if el==numero:
                freq=freq+1
    return freq