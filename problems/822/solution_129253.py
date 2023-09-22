def repetidos(lista):
    i=0
    resultado=0
    while i<len(lista):
        if lista[i] in lista[0:i-1]:
                resultado=resultado+1
        i=i+1
    return resultado