def conta_numero(numero,matriz):
    '''a funcao retorna quantas vezes o numero aparece na matriz
    int, list -> int'''
    contagem=0
    for i in range(len(matriz)+1):
        if numero in matriz[i][0:-1]:
            contagem=1+contagem           
    return contagem