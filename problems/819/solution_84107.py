def filtraMultiplos(numeros, numero):
    multiplos=[]
    i=0
    while i < len(numeros):
        if numeros[i] % numero == 0:
            multiplos.append(numeros[i])
        i=i+1
    return multiplos