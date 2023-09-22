def repetidos(lista):
    i=0
    quantidade=0
    while i<len(lista):
        if lista[i]==lista[i+1]:
            quantidade[i]=quantidade[i+1]
        i=i+1
    return quantidade