#2
def conta_numero(numero,matriz):
    '''retorna quantas vezes um numero aparece em uma matriz
    matriz -> int'''
    contador = 0
    for i in matriz:
        for i2 in i:
            if i2 == numero:
                contador += 1
    return contador