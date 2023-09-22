def conta_numero (numero, matriz):
    '''list, int -->int'''
    contador = 0
    for i in matriz:
        contador += i.count(numero)
    return contador