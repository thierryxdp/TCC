def repetidos(numeros):
    duplas=0
    i=0
    while i<len(numeros):
        if numeros[i]==numeros[5]:
            duplas+=1
            i+=1
        else:
            i+=1
    return duplas