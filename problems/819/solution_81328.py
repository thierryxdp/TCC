def filtraMultiplos(lista, n):
    """retorna uma lista com os números múltiplos de 'n'"""
    Nlista = []
    numero = 0
    while numero < len(lista):
        if lista[numero]% n == 0:
            Nlista = Nlista + [lista[numero],]
        numero = numero + 1
    return Nlista