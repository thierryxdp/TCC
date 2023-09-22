def conta_numero(numero,matriz):
    '''Recebe um número inteiro e uma matriz formada por números
    inteiros e retorna a quantiidade de vezes que o número informado
    aparece na matriz; int, list(list) -> int'''
    contador = 0
    for i in matriz:
        for j in matriz[i]:
            if j == numero:
                contador += 1
    return contador