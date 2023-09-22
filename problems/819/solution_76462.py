def filtraMultiplos(numeros, n):
    '''função que recebe uma lista e um numero n e retorna os 
    numeros da lista que são multiplos de n'''
    resultado = []
    c = 0
    while c < len(numeros):
        if numeros[c] % n == 0:
            resultado = resultado + numeros[c]
        c += 0