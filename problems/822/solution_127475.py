def repetidos(lista):
    i=0
    a=0
    while i<len(lista)-2:
        if lista[i]==lista[i+1] and lista[i]!=lista[i+2]:
            a+=1
        i+=1
        if lista[i]==lista[i+1] and lista[i-1]!= lista[i+1] and i==len(lista)-2:
            a+=1
    return a