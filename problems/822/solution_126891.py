def repetidos(lista):
    i=0
    resultado=[]
    while i<len(lista):
        if lista[i+1]==lista[i]:
            resultado += 1
    return resultado