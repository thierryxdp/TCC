def conta_numero (numero, matriz):
    '''Funcao que, dado um numero e uma matriz, conta e retorna quantas vezes esse numero aparece na matriz.
    int, list -> int'''
    
    contador = 0
    for linha in matriz:
        for i in linha:
            if i == numero:
                contador += 1
    return contado