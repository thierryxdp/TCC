def faltante(lista):
    for i in range(len(lista)+1):
        if lista[i+1] ==  i+1:
            return i+1