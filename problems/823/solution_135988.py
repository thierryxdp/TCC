def faltante(lista):
    i=0
    while i<len(lista):
        if lista[i]!= lista[i-1]+1:
            return lista[i-1]+1
        else:
            i+=1