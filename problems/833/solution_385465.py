def conta_numero(numero,matriz):
    '''Dados um número e uma matriz de inteiros de tamanho 
    qualquer, conta e retorna quantas vezes aquele número 
    aparece na matriz
    int, list -> int '''
    total = 0
    for i in matriz:
        for j in i:
            if numero == j:
                total = total + 1
    return total