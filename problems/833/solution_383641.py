def conta_numero(numero, matriz):
    '''retorna quantas vezes o numero aparece 
    na matriz; int, list -> int'''
    nVezes=0
    n=0
    while n< len(matriz):
        for i in matriz[n]:
            if matriz[n][i]==numero:
                nVezes+=1
        n=n+1
    return nVezes