def conta_numero(numero, matriz):
    '''retorna quantas vezes o numero aparece 
    na matriz; int, list -> int'''
    nVezes=0
    n=0
    i=0
    while n< len(matriz):
        while i<len(matriz[n]):
            if matriz[n][i]==numero:
                nVezes+=1
            i=i+1
        n=n+1
    return nVezes