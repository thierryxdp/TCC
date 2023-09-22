def conta_numero (matriz, n):
    '''list, int -->int'''
    contador = 0
    for i in matriz:
        contador += i.count(n)
    return contador