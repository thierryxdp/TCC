def faltante(lista):
    i=0
    
    while i<len(lista)-1:
        if lista[i+1] != lista[i] +1:
            return lista[i+1]
        i+=1
    return lista