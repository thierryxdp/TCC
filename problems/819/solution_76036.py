def filtraMultiplos (lista, n):
    divisiveis = ()
    numero = 0
    while numero % n != 0 :
        if lista[numero] in numero % 0:
            divisiveis = divisiveis + lista [numero]
        numero = numero + 1
    return divisiveis