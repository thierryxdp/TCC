def repetidos(lista):
    i = 0
    lista_nova = []
    while i<len(lista):
        if lista[i] == lista[i - 1]:
            lista_nova.append(1)
            i=i+1
            return len(lista_nova)