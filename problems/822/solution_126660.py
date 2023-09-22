def repetidos(numeros):
    duplas=0
    i=0
    while (i-1)<len(numeros):
        if numeros[i]==numeros[i+1]:
            duplas+=1
            i+=1
        else:
            i+=1
    return duplas