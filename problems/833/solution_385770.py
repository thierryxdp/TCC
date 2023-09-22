def conta_numero(n, matriz):
    '''Funcao que conta e retorna a quantidade de vezes que um numero inteiro
n aparece em uma dada matriz de entrada.
int, list -> int'''
    if matriz == []:
        return 0
    
    quantidade = 0
    for elem in matriz[0]:
        if list.count(matriz[elem],n)!=0:
            quantidade += list.count(matriz[elem],n)
    return quantidade