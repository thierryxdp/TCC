def repetidos(lista):
    quant=[]
    i=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            list.append(quant,lista[i])
        i=i+1
    return len(quant)