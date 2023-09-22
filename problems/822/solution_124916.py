def repetidos (lista):
    num_repetidos=[]
    i=0
    while i<(len(lista)-1):
        if lista[i]==lista[i+1]:
           num_repetidos=num_repetidos+[i,]
        i=i+1
    return len(num_repetidos)