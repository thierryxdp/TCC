def conta_numero (numero,matriz):
    '''retorna quantas vezes o número aparece na matriz'''
    j = 0
    vezes = 0
    for linhas in matriz:
        for elementos in linhas:
            
            if numero == elementos:
                vezes = vezes + 1
                j = j + 1
            elif numero != elementos:
                j = j + 1
                vezes = vezes
            
    return vezes