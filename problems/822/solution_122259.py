def repetidos(lista):
    i=0
    repetidos = []
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repetidos.append(lista[i])
        i+=1
    return len(repetidos)