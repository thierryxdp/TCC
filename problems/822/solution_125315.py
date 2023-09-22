def repetidos(lista):
    i=0
    lista=[]
    lista.sort()
    while i < len(lista):
        if lista[i] != lista[i+1]:
            cont=+1
            i=+1
            return cont