def filtraMultiplos(lista,n):
    multiplos = ()
    numero = 1
    while numero > 0:
        if lista[numero] / n:
            multiplos = multiplos + (lista[numero])
        numero = numero + 1
    return multiplos