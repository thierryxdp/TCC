def conta_numero(n,matriz):
    '''função em que dado um número (n) e uma matriz de inteiros de tamanho
    qualquer, conta e retorna quantas vezes aquele número aparece na matriz;
    int, list -> int'''
    q=0
    for i in range(len(matriz)):
            if n in matriz[i]:
                q+=list.count(matriz[i],n)
    return q