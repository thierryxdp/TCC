def conta_numero(numero, matriz):
    '''dado um numero inteiro e uma matriz de inteiros, retorna
    quantas vezes aquele numero aparece na matriz
    int,list->int'''
    
    conta=0
    
    for i in matriz:
        for j in i:
            if numero==j:
                conta=conta+1
    return conta