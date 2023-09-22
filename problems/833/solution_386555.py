def conta_numro(numero, matriz):
    '''Dado um número inteiro e uma matriz de inteiros, retorna 
    quantas vezes aquele número aparece na matriz.
    int, list -> int'''
    acumul = 0
    for linha in matriz:
        for termo in linha:
            if termo == numero:
                acumul+=1
    return acumul