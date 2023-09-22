def repetidos(lista):
    aux = 0
    i = 0
    while i < len(lista):
        if i != 0 :
            if lista[i+1] == lista[i]:
                aux += 1
        i += 1