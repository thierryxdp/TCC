def conta_numero(numero,matriz):
    '''função que dado um número inteiro  e uma matriz de inteiros conta e retorna quantas vezes esse numero aparece na matriz
    int,list-> int'''
    numeros=0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if numero in matriz[i]:
                numeros+=1
    return numeros