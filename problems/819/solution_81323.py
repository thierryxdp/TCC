def filtraMultiplos(lista, n):
    Nlista = ()
    numero = 0
    while numero < len(lista):
        if lista[numero]% n == 0:
            Nlista = Nlista + (lista[numero],)
        numero = numero + 1
    return Nlista