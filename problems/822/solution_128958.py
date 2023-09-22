def repetidos(lista):
    i=0
    
    while i<= len(lista):
        ocorrencias=0
        if lista[i]==lista[(i+1)]:
            ocorrencias=ocorrencias+1
        i=i+1
    return ocorrencias