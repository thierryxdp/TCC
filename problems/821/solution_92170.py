def fatorial(lista):
    numero = lista[0]
    fatorial = 1
    while(numero > 0):
        fatorial = fatorial * numero
        numero = numero - 1
    return fatorial