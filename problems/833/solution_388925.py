def conta_numero(numero,matriz):
    '''Recebe um número inteiro e uma matriz contendo números inteiros
    e retorna quantas vezes o número aparece na matriz 
    (int, list -> int)'''
    contador = 0
    for linha in matriz:
        for aij in linha:
            if aij == numero:
                contador = contador + 1
    return contador