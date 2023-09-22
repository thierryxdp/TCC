def conta_numero(numero,matriz):
    '''Dado um numero inteiro e uma matriz de inteiros 
    de tamanho qualquer, conta e retorna quantas vezes aquele 
    numero aparece na matriz
    int, list -> int'''
    
    soma=0
    n_linha=len(matriz)
    
    if n_linha ==0:
        return 0
    
    n_col=len(matriz[0])
    
    for i in range(n_linha):
        for j in range(n_col):
            if matriz[i][j]==numero:
                soma+=1
    return soma