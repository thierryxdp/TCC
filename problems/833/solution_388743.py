def conta_numero(numero, matriz):
    ''' 
    Recebe um inteiro e uma matriz
    Retorna quantas vezes aquele numero aparece na matriz
    '''
    cont = 0
    for k_elemen in matriz:
        for i in k_elemen:
            if(i == numero):
                cont += 1
    return cont