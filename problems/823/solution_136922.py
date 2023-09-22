def faltante(lista):
    i=0
    while i < len(lista):
        lista.sort()
        if i + 1 != lista[i]:
            return i+1
        i=i+1