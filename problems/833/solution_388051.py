def conta_numero(numero,matriz):
    '''
    função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz;
    int, list(list) -> int
    '''
    aparece = 0
    for linha in matriz:
        for aij in linha:
            if aij == numero:
                aparece = aparece + 1
    return aparece