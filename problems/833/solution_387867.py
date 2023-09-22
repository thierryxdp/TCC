def conta_numero(numero,matriz):
    '''função que dado um número inteiro  e uma matriz de inteiros conta e retorna quantas vezes esse numero aparece na matriz
    int,list-> int'''
    repeticoes=0
    numeros=0
    mais=0
    for i in matriz[i]:
        if numero == i:
            for j in matriz[i][j]:
                if numero == j:
                    repeticoes +=1
    return repeticoes