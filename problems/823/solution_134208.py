def faltante(lista):
    i=0
    while i<len(lista)-1:
        if abs((lista[i])-(lista[i+1]))!=1:
            return lista[i+1]-1
        i=i+1