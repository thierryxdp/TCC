def conta_numero(numero, matriz):
    '''Retorna o numero de vezes que um numero inteiro aparece dentro de uma matriz'''
    #int, list -> int
    quantidade = 0
    for linha in matriz:
        for Aij in linha:
            if Aij == numero:
                quantidade = quantidade + 1
    return quantidade