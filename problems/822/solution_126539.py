def repetidos(lista):
    i=0
    quantas_vezes=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            quantas_vezes=quantas_vezes+1
        i=i+1
    return quantas_vezes