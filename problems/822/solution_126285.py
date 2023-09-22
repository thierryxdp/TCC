def repetidos(lista):
    i=1
    repeticoes=0
    while i<len(lista):
       if lista[i]==lista[i-1]:
        repetições+=1
        i+=1
    return repeticoes