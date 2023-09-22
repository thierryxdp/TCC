def conta_numero(numero, matriz):
    '''retorna quantas vezes o numero aparece 
    na matriz; int, list -> int'''
    nVezes=0
    for j in matriz:
        for i in matriz[j]:
            if matriz[j][i]==numero:
                nVezes+=1
    return nVezes