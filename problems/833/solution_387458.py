def conta_numero(numero,matriz):
    '''a funcao retorna quantas vezes o numero aparece na matriz
    int, list -> int'''
    for i in range(len(matriz)+1):
        if numero in matriz[0:-1]:
            contagem=1+contagem           
    return contagem