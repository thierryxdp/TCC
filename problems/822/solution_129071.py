def repetidos(lista):
    duplicados=[]
    for i in range(len(lista)):
        if lista.index(lista[i])!=i:
            duplicados.append(lista[i])
            return duplicados