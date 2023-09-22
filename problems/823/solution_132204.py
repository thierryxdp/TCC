def faltante(lista):
    lista2=range(1,len(lista)+1)
    i=0
    while i<len(lista2):
        if lista2[i] not in lista:
            return lista2[i]
    	i=i+1