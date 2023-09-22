def conta_numero(numero,matriz):
    '''recebe um inteiro e uma matriz e retorna quantas vezes o número aparece na matriz.
    (list(list),int) -> int'''
    cont = 0
    for lista in matriz:
        for elemento in lista:
            if elemento == numero:
               cont = cont + 1
    return cont