def faltante(lista):
    i=1
    while i<=len(lista):
        if lista[i-1]==i:
            i+=1
        else:
            return i
   
    return i+1