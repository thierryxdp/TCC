def repetidos(lista):
    i=0
    quantidade=0
    while i<len(lista):
        if lista[i]+1==lista[i]:
            quantidade[i+1]=quantidade[i]
        i=i+1
    return quantidade