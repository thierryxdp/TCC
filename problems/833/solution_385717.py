def conta_numero(n, matriz):
    '''Funcao que conta e retorna a quantidade de vezes que um numero inteiro
n aparece em uma dada matriz de entrada.
int, list -> int'''
    lin = len(matriz)
    col = len(matriz[0])
    quantidade = 0
    for i in range(lin):
        if list.count(matriz[0],n)!=0:
            quantidade += list.count(matriz[i],n)
    return quantidade