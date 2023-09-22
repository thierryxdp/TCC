def faltante(lista):
    i=0
    while i < len(lista):
        lista.sort()
        if (lista[i+1])!=(lista[i]+1):  
            return lista[i]+1
        elif (lista[i-1])!=(lista[i]-1):
            return lista[i]-1
        i=i+1