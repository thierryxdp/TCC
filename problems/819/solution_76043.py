def filtraMultiplos (lista, n):
    divisiveis = [ ]
    a = list divisiveis
    numero = 0
    while numero % n == 0 :
        if lista[numero] % n == 0:
            a = a + lista[numero]
        numero = numero + 1
    return a