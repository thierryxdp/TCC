def filtraMultiplos(lista,n):
    '''uma função que filtra o multiplos de um numero n, retornando uma lista apenas com os 
    numeros filtrados.
    lista + int -> lista'''
    contador = 0
    acumulador = []
    while contador < len(lista):
        if lista[contador]%n = 0:
            acumulador += lista[contador]
            contador += 1
        else:
            contador += 1
    return acumulador