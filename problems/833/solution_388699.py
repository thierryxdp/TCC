def conta_numero(numero,matriz):
    '''funcao que,dada uma matriz de inteiros e um numero inteiro,
    retorna quantas vezes esse numero aparece na matriz;
    list(list),int-->int'''
    vezes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                vezes=vezes+1
    return vezes