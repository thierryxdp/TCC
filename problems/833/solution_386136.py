def conta_numero(numero,matriz):
    '''Recebe um número inteiro e uma matriz. Retorna
    quantas vezes o número aparece na matriz.
    int, list -> int'''
    contador = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                contador += 1
    return contador