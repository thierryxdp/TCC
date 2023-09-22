def repetidos(lista):
    i=0
    resultado=0
    while i<len(lista):
        if lista[i] in lista[i-2:i-1]:
                resultado=resultado+1
        i=i+1
        return resultado