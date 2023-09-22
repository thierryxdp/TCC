def filtraMultiplos(lista,n):
    multiplos = ()
    elemento = 0
    while elemento <len(lista):
        if lista[elemento]%n == 0:
            multiplos = multiplos + (lista[elemento],)
        elemento = elemento + 1
    return multiplos