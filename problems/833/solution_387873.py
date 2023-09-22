def conta_numero(numero,matriz):
    '''função que dado um número inteiro  e uma matriz de inteiros conta e retorna quantas vezes esse numero aparece na matriz
    int,list-> int'''
    repeticoes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j]
            if numero in matriz:
                repeticoes+=1      
    return repeticoes