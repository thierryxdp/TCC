def repetidos(lista):
    v=0
    repetidos = []
    while v < len(lista):
        if lista[v] == lista[v-1]:
            repetidos.append(lista[v])
        v+=1
    return len(repetidos)