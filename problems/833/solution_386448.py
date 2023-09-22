def conta_numero(nint,matriz):
    '''Dado um numero inteiro e uma matriz de inteiros, retorna a quantidade de vezes que o numero aparece
    na matriz; int, list[list] -> int'''
    i=0
    n=0
    for linha in matriz:
        j=0
        for col in matriz[i]:
            if matriz[i][j] == nint:
                n+=1
            j+=1
        i+=1
    return n