def filtraMultiplos(listado,n):
    multiplos = ()
    numero = 1
    while numero > 0:
        if listado[numero] / n:
            multiplos = multiplos + listado[numero]
        numero = numero + 1
    return multiplos