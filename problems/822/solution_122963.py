def repetidos(lista):
    contador=0
    i=0
    while contador<=len(lista):
        if lista[contador]==lista[contador-1]:
            contador=contador+1
        	i=i+1  
    return i