def repetidos(lista):
    contador=0
    i=0
    while contador<len(lista):
        if lista[contador+1]>lista[contador]:
            lista[contador-1]==lista[contador]
        elif lista[contador+1]==lista[contador]:
        	i=i+1 
        else:
            i
        contador=contador+1
    return i, contador