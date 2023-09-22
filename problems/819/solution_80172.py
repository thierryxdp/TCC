def filtraMultiplo(numeros, n):
    multiplos=()
    numero=0
    while numero<len(numeros):
        if numero % n==0:
            multiplos = multiplos + (numeros[numero],)
    numero= numero + 1
    return multiplos