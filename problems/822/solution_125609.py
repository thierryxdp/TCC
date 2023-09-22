def repetidos(numeros):
    multiplos = numeros
    multiplos=[]
    i=0
    while i<len(numeros):
        if numeros[i] == numeros[i+1]:
            multiplos.append(numeros[i])
        i=i+1
    return multiplos