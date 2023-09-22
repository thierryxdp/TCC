def faltante(lista):
    i = 0
    while i < len(lista):
        if i != lista[i]-1:
            return i+1
        i+=1