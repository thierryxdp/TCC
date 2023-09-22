def filtraMultiplos(numeros,n):
    numeros = []
    for nmr in numeros:
        if nmr%n == n:
            return nmr