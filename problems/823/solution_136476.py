def faltante(numeros):
    i=0
    list.sort(numeros)
    if numeros[0]!=1:
            return 1
    while i<len(numeros):
        if numeros[i]+1!=numeros[i+1]:
            return numeros[i]+1
        if numeros[i]+1==numeros[i+1]:
            return len(numeros)+1
        i+=1