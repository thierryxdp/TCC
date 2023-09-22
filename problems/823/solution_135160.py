def faltante(lista):
    list.sort(lista)
    lista1=lista[:]
    i=0
    while i<len(lista1):
        if lista1[i]-i==1:
    		i=i+1
    		return i+1
        if lista1[i]-i==2:
            return i+2