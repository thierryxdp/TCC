def faltante(lista): 
    i=0
    while i < len(lista):
        if (lista[i+1]-lista[i])!=1:
            resultado=lista[i]+1 
        i=i+1
    return resultado